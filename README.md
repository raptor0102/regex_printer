# regex_printer
Search for matching regex in files and print the result

As requested I provided a Makefile and to run the project you should easily use ```Makefile build``` and ```Makefile run```.
How to use:

Once you are in your developing environment pull this project from git or just copy all the project into your machine.
Once you have all the project, go to Docker folder and simply run:

```Makefile build``` -> Which build your image container environment for the first time with all python necessary modules described  
then run:
        ```Makefile run```

Then, for every change in your code (regex_printer tool or in the tests) you can simply run again:
        ```Makefile run```

build and run
If I run ```docker-compose up``` the first time everything works fine, however, when one change the code after the first time, the changes will not reflect in the container that runs. This is because upon each ```docker-compose up``` command, compose will look for lasters taged image (that already exists) and does not build a new image and creates a container based on the old one. As I need that image name and tag to publish/deploy my image, I instead use:

```docker-compose up --build```
It will re-build an image with the changes reflected. Every time one make some changes, I will run ```docker-compose up --build``` and a new fresh image is created that can be seen with ```docker images```. (although the name and tag remain unchanged, changes can be found in the image id that this is a fresh new image).

Currently ```Makefile run``` will generate a new fresh image and use this image to run the container which executing all the unittests suite I created.


The project includes the following files:

/Docker/

        Makefile
        Dockerfile
        docker-compose.yml
        requirements.txt
        deploy.env

/Docker/src/

        main.py
        RegexPrinter.py
        utils.py
        __init__.py


/Docker/tests/

        test_input_args.py
        test_the_output_machine_mode.py
        test_the_output_no_color.py
        test_the_output_with_color.py
        __init__.py
        dummy_input1.txt
        dummy_input2.txt
        dummy_input3.txt
        dummy_input4.txt
        dummy_output1_machine.txt
        dummy_output1_no_color.txt
        dummy_output1_with_color.txt
        dummy_output2_machine.txt
        dummy_output2_no_color.txt
        dummy_output2_with_color.txt
        dummy_output3_machine.txt
        dummy_output3_no_color.txt
        dummy_output3_with_color.txt
        dummy_output4_machine.txt
        dummy_output4_no_color.txt
        dummy_output4_with_color.txt


Assumptions:

1.	When receiving as an input only file/files and regex, the output will be to the standard output while each match is printed in different line.
2.	When receiving as an input file/files, regex and a color, the output will be to the standard output while all text matches within a single line will be colored the single line.
3.	When receiving as an input file/files, regex and a machine flag, the output will be to the standard output as in machine formatted you requested.
4.	The argparse Module of python will execute all the input correctness such as: 
•	file/s are existing and in 'read' mode permission.
•	At least single file provided.
•	The regex expression is valid.
•	The -c and -m inputs are mutually_exclusived as requested.
•	Correctness for the color.
5.	-m/--machine flag can be sent both as a unique value such as -m without any follow indicating parameter and also as a follow parameter which can be any given true signal such as: 'yes', 'true', 't', 'y', '1', 'True'. All are handled.
6.	While the user determines to send colder such as: -c, the color can be either: -c BLUE, -c blue or -c 34 -c Blue, -c blUE, -c BLue etc. if the value is not valid correct message will be sent to the user.
7.	I read each file in parallel using the threading module. Thus that in case of large number of files (without dependencies) it will be faster with the python GIL mechanism.
8.	I read each file line by line and not using the 'realines' function, thus because the fact that files can be large and we will enter memory usage problems.
9.	I split the the project objects for three:
        ```main.py```
        ```RegexPrinter.py```
        ```utils.py```
        In order to use the module please run the main.py file (with the relevant input).
        For encapsulation the class inside the RegexPrinter.py file:
        
        class RegexPrinter(object)      
        class RegexPrinterByColor(RegexPrinter)
        class RegexPrinterMachine(RegexPrinter)
      The ```unitls.py``` file parse the input paramters.

10.     I created 19 unittests within 4 files. ```test_input_args.py``` testing some input combinations.
        and the other three tests the correct output for regular/colored/machine output.





