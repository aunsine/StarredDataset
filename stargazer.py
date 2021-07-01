import GitHubAPI
import log 
import getopt
import sys

logger = log.setup_logger()

def main():
    argv = sys.argv[1:]     
    username = ''
    repo_name = ''
    
    logger.info('--- start parameter validation --')  
    
    try:
        opts, args = getopt.getopt(
            argv, "hu:r:", ["user_name=", "repo_name="])
    except getopt.GetoptError:
        print('Usage: python stargazer.py -u <user_name> -r <repository_name>')
        sys.exit(2)

    #Assign argument
    for opt, arg in opts:
        if opt == '-h':
            print( 'Usage: python stargazer.py -u <user_name> -r <repo_name>')
            sys.exit()
        elif opt in ('-u', '--user_name'):
            username = arg.strip()
        elif opt in ('-r', '--repo_name'):
            repo_name =  arg.strip() 

    if username == '' or repo_name == '':
        print("GitHub username and repository name both are required! Run 'stargazer -h' for help")
        sys.exit()

    if username != '' and repo_name != '':
        gh_api_obj =  GitHubAPI.GitHubAPI(username=username, repo_name=repo_name) 
        gh_api_obj.get_stargazer_data()

    
    logger.info('--- end parameter validation --')  

if __name__ == "__main__":
    main() 