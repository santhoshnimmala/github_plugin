<!--Murex Copyright disclaimer-->
<!-- 
Copyright Murex S.A.S., 2003-2019. All Rights Reserved.

This software program is proprietary and confidential to Murex S.A.S and its
affiliates ("Murex") and, without limiting the generality of the foregoing
reservation of rights, shall not be accessed, used, reproduced or distributed
without the express prior written consent of Murex and subject to the
applicable Murex licensing terms.

Any modification or removal of this copyright notice is expressly prohibited. 
-->
<!--Murex Copyright disclaimer-->
# Git Server Plugin Implementation

## Overview
MXpipeline provides a Service Provider Interface for the Git Server implementations of different CI processes.


## How to start the implementation?

### Step 1:
Place the Configuration and CI repository of the project on the Git Server.

### Step 2:
Create the Git Server Plugin directory by copying it from the templates folder: templates/git_server_plugin and naming it based on the Git Server vendor name.

### Step 3:
Comment out or remove the error throwing from the seed.py under [git_server_vendor/config/seed.py](config/seed.py)

    ```yaml 
    # Call the git server api(s) to create the needed webhooks, etc... 
    # raise NotImplementedError
    ```

### Step 4:
Host the Git server plugin folder created in step 3, on the git server as a git repository where it will be maintained.

### Step 5:
Under CI repository: <br/>
- mxpipeline/downloader/inventory.yml:
    - Point to a specific MXpipeline artifact by specifying the MXpipeline product source, url and directory.
        ```yaml
        ###############################################
        ###### DOWNLOAD FROM ARTIFACT REPOSITORY ######
        ###############################################
          # # Uncomment and fill this section to download mxpipeline from an artifact repository
          mxpipeline:
            source: artifact_repository
            url: "https://xyz/{{ mxpipeline_version }}/mxpipeline-{{ mxpipeline_version }}.tar.gz"
            directory: "{{ playbook_dir }}/.."
        ```
    - Point to a specific Git Server plugin artifact: 
        
        1. Plugin is available on an artifact repository: specify the plugins name, url and source.

            ```yaml
            plugins:
              ###############################################
              ###### DOWNLOAD FROM ARTIFACT REPOSITORY ######
              ###############################################
              - name: "azure_repos"
                url: "https://xyz/repos-plugin-1.0.0.tar.gz"
                source: artifact_repository
            ```


        2. Plugin is on the git repository: specify the name, url, version and source

            ```yaml
            plugins:
              ###############################################
              ######## DOWNLOAD FROM GIT REPOSITORY #########
              ###############################################
              - name: azure_repos
                url: https://xyz/repo-plugin.git
                version: master
                source: git
            ```
 
- mxpipeline/ci_server_config/inventory.yml:
    - Fill the git_provider by the corresponding git server vendor name.
        ```yaml
        #############################
        ### GIT PLUGIN PARAMETERS ###
        #############################

        git_provider: 'azure_repos'
        ```

### Step 6:
Run Orchestrator instance with the corresponding CI configuration environment variables (specify the Git Server Repository URL and credentials).


### Step 7:
Make sure the seed is executed and green.

### Step 8:
You are now ready to start implementing any CI process that is available in SPI mode. 