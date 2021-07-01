# StarredDataset
Get starred info of a given repository and export to excel.

# Required library
Please install following "json"(version 2.0.9 or higher) and "pandas" (version 1.0.5 or higher)

    pip install json

    pip install pandas

# Deployment and how to execute

1. Download source code and place in a desired directory (Ex. D:\Me\Learning\Git_Stargazer)

![image](https://user-images.githubusercontent.com/73420344/124177833-f8649880-dada-11eb-9513-0942f4e2ee96.png)



2. Go to run, type "cmd" to open command prompt window and change working directory to the previous path.

![image](https://user-images.githubusercontent.com/73420344/124178017-3792e980-dadb-11eb-81c0-bd1d9ef6759f.png)


3. Execute program, there are 2 mandatory parameters.

    3.1 username : following by option  '-u' or --user_name'
    
    3.2 repo_name : following by option '-r' or '--repo_name'

    **Sample** 
    
        python stargazer.py -u aunsine -r MyRepo
        
    **Expected result**        
![image](https://user-images.githubusercontent.com/73420344/124177604-a885d180-dada-11eb-9eb4-2a41b597a18c.png)

4. Dataset will be written in "output" folder.
    **Sample output file**
    ![image](https://user-images.githubusercontent.com/73420344/124178840-2e564c80-dadc-11eb-9d94-a69a9dbe7679.png)

    

# Validation
 - Invalid parameter
 
 ![image](https://user-images.githubusercontent.com/73420344/124178270-935d7280-dadb-11eb-9da3-44c2f02dbeba.png)


 - Not exist Github username and/or repository name

![image](https://user-images.githubusercontent.com/73420344/124178306-9d7f7100-dadb-11eb-9280-50104991ee04.png)


 - Invalid option

![image](https://user-images.githubusercontent.com/73420344/124178332-a4a67f00-dadb-11eb-8641-e217a1cde354.png)
 
