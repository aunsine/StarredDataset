import sys 
import getopt
import json 
import shlex
import subprocess
import pandas as pd
   
def get_stargazer_data():
    try:
        import pdb;pdb.set_trace()

        cmd = f'''curl -H "Accept: application/vnd.github.v3.star+json" https://api.github.com/repos/{username}/{repo_name}/stargazers'''
        args = shlex.split(cmd)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = process.communicate()[0]
        exit_code = process.wait()

        if exit_code == 0:
            # Decode UTF-8 bytes to Unicode, and convert single quotes 
            # to double quotes to make it valid JSON
            my_json = stdout.decode('utf8').replace("'", '"')            

            # Load the JSON to a Python list & dump it back out as formatted JSON
            data = json.loads(my_json)

            #Convert response into dataset
            my_list = []
            for i in range(0,len(data)):
                my_dict = {'starred_at': data[i]['starred_at'] }
                my_dict.update(
                    login = data[i]['user']['login'],
                    id =  data[i]['user']['id'] ,
                    organizations_url = data[i]['user']['organizations_url']  ,
                    user_type = data[i]['user']['type']   
                )
                my_list.append(my_dict)

            df = pd.DataFrame(my_list)
            
            try:
                    
                # create excel writer object
                writer = pd.ExcelWriter('output.xlsx')
                # write dataframe to excel
                df.to_excel(writer)
                # save the excel
                writer.save()
                print('Stargazer dataset is written successfully to Excel File.')

            except Exception as ex:
                print( f'Error at print excel file >> {ex}' )

        else:
            print('Failed at call GitHub API')

    except Exception as e :
        print(f'Error at execute get_stargazer_data {e} ')
 

def main():
    argv = sys.argv[1:]
    global username, repo_name 
    username = ''
    repo_name = ''

    import pdb;pdb.set_trace()
    try:
        opts, args = getopt.getopt(
            argv, "hu:r:", ["user_name=", "repo_name="])
    except getopt.GetoptError:
        print('Usage: python stargazers.py -u <user_name> -r <repository_name>')
        sys.exit(2)
      
    #Assign argument
    for opt, arg in opts:
        if opt == '-h':
            print( 'Usage: python stargazers.py -u <user_name> -r <repo_name>')
            sys.exit()
        elif opt in ('-u', '--user_name'):
            username = arg.strip()
        elif opt in ('-r', '--repo_name'):
            repo_name =  arg.strip() 

    if username == '' or repo_name == '':
        print("GitHub username and repository name both are required! Run 'stargazer -h' for help")
        sys.exit()

    if username != '' and repo_name != '':
        get_stargazer_data()
  


if __name__ == "__main__":
    main()
