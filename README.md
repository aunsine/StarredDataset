# StarredDataset
Get starred info of a given repository and export to excel.

# Required library
Please install following "json"(version 2.0.9 or higher) and "pandas" (version 1.0.5 or higher)

    pip install json

    pip install pandas

# Deployment and how to execute

1. Download source code and place in a desired directory.
2. Open command prompt window and change working directory to the previous path.
3. Execute program, there are 2 mandatory parameters 

    3.1 username : following by option  '-u' or --user_name'
    3.2 repo_name : following by option '-r' or '--repo_name'

    Sample 
    
        python stargazer.py -u aunsine -r MyRepo
