Hello! This is an end-to-end project for Text summarization and the setup might look overwhelming at once. So I will explain the entire process step by step.

## Initial setup steps

1. Instead of manually creating folders, we used the 'os' library to create directories, constructors and files in template.py and we executed it.
2. Configuring the setup.py for disributing the project as a package and installing the requirements.txt
3. Created custom logging, in the constructor file inside the logging module. Can import the logging object anywhere and can experiment.
4. The functions that we will use the most, are written inside the common.py of utils module. Eg: read_yaml, create_directories etc.
   (We have used ConfigBox and BoxExceptionError)

## Workflows
1. Update config.yaml file
2. Update params.yaml file
3. Update entity constructor
4. Update configuration manager in src/config/configuration.py
5. Update the component
6. Update Pipeline
7. Update main.py

Finally, update app.py
