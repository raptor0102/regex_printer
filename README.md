# regex_printer
Search for matching regex in files and print the result

As requested I provided a Makefile and to run the project you should easily use Makefile build and Makefile run.
How to use:

Once you are in your developing environment pull this project from git or just copy all the project into your machine.
Once you have all the project, go to Docker folder and simply run:

Makefile build -> Which build your image contrainer environment for the first time with all python necessary modules described  

Makefile run

Then, for every change in your code (regex_printer tool or in the tests) you can simply run again:
Makefile run

build and run
If you run docker-compose up the first time everything works fine, however, when you change the code after the first time, the changes will not reflect in the container that runs. This is because upon each docker-compose up command, compose will look for lasters taged image (that already exists) and does not build a new image and creates a container based on the old one. As we need that image name and tag to publish/deploy our image, we need to instead use:

docker-compose up --build
It will re-build an image with the changes reflected. Every time you make some changes, run it and a new fresh image is created that can be seen with (note that although the name and tag remain unchanged, change in image id shows that this is a new image):


The project includes the following files:

/Docker/

        Makefile
        Dockerfile
        docker-compose.yml

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

1. search_regex_in_file_script.py
2. Makefile
3. Dockerfile
4. requirements.txt # which include the requirements for the non standard python library required for the project
Assumptions:

Part 1:

1. When receiving as an input only file/files and regex, the output will be to the standard output while each match is printed in different line.
2. When receiving as an input file/files, regex and a color, the output will be to the standard output while all text matches will be colored inside the full line print.
3. When receiving as an input file/files, regex and a machine flag, the output will be to the standard output as in machine formatted you requested.
4. -m/--machine flag only indicates of True/False input. Without any additional parameters.
5. While the user determine to send colder such as: -c, the color can be either: -c BLUE, -c blue or -c 34.
6. All the combinations of the inputs from the command line is done by the argparse. most code is in function: handling_cmd_args.
7. I print only suffix filename that out  or your full file name full output to the standard out file names as in they were  output I printed then
8. I created
9. I read each file in parallel, in case of large number of files (without dependencies) it will be faster with the python GIL mechanism.


Part 2:

1. My AWS is noy valid any more. I used it more than a year, for I tryied to work on TBM could.

