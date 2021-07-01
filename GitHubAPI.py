
'''
This python script is used to get stargazer info and convert into a flat file.
'''

import sys 
import json 
import shlex
import subprocess
import pandas as pd
import log as log 
import datetime
import os

logger = log.setup_logger()


class GitHubAPI:
    username =''
    repo_name = ''
    
    def __init__(self, username, repo_name):
        self.username = username
        self.repo_name = repo_name
      

    def get_stargazer_data(self):
        
        logger.info('--- start get_stargazer_data --')  
        try:

            #Call GitHub API to get stargazer data
            cmd = f'''curl -H "Accept: application/vnd.github.v3.star+json" https://api.github.com/repos/{self.username}/{self.repo_name}/stargazers'''
            args = shlex.split(cmd)
            process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout , stderr  = process.communicate()
            exit_code = process.wait()
            
            #Check result code from API requesting(0 ==> OK)
            if exit_code == 0:
                
                # Decode UTF-8 bytes to Unicode, and convert single quotes 
                # to double quotes to make it valid JSON
                my_json = stdout.decode('utf8').replace("'", '"')            

                # Load the JSON to a Python list & dump it back out as formatted JSON
                data = json.loads(my_json)
                
                if isinstance(data,dict) and data['message'] =='Not Found' :
                    print(f'There is not Github username [{self.username}] and/or repo. name [{self.username}]')
                    sys.exit(2)

                #Convert response into dataset
                my_list = []
                for i in range(0,len(data)):
                    str_starred_at =  data[i]['starred_at'] 
                    dt_starred_at = datetime.datetime.strptime(str_starred_at,'%Y-%m-%dT%H:%M:%SZ')

                    #initial dictionary object with repository name and owner
                    my_dict = {'repo_name': self.username , 'repo_owner': self.username }

                    #update the dictionary object with stargazer info.
                    my_dict.update(
                        login = data[i]['user']['login'],
                        id =  data[i]['user']['id'] ,
                        organizations_url = data[i]['user']['organizations_url']  ,
                        user_type = data[i]['user']['type'],
                        starred_at = str_starred_at,
                        starred_at_year = dt_starred_at.year,
                        starred_at_month = dt_starred_at.month,
                        starred_at_date = dt_starred_at.day,
                        starred_at_hour = dt_starred_at.hour,
                        starred_at_min =  dt_starred_at.minute,
                        starred_at_sec = dt_starred_at.second                   
                    )

                    my_list.append(my_dict)

                df = pd.DataFrame(my_list)
                
                logger.info('--- start Saving file --')
                try:
                    # prepare path for saving output file
                    output_path = os.getcwd() +  "\\output\\"                  
                    if os.path.isdir(output_path) == False:
                        os.makedirs(output_path) 

                    # create excel writer object
                    writer = pd.ExcelWriter(output_path +f"stargazer_{datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')}.xlsx")
                    # write dataframe to excel
                    df.to_excel(writer)

                    # save the excel
                    writer.save()
                    print('Stargazer dataset is written successfully to Excel File.')

                except Exception as ex:
                    logger.error(f'Error at print excel file >> {ex}')  
                    print( f'Error at print excel file >> {ex}' )                    
                logger.info('--- end Saving file --')

            else:
                logger.error(f'''Failed at Call GitHubAPI >> { stderr.decode('utf8').replace("'", '"')   }''')
                print('Failed at call GitHub API')

        except Exception as e :
            logger.exception(e)
            print(f'Error at execute get_stargazer_data {e} ')
    
        
        logger.info('--- start get_stargazer_data --')  