# MIRO communication application  
## Built using the Writing Tech For Jarrod (wtfj) module  

![Jarrod](https://github.com/WritingTechForJarrod/app/blob/master/img/readme1.jpg?raw=true "wtfj")  
### This is Jarrod
Jarrod is an incredibly determined, charismatic individual who happens to suffer from Multiple Sclerosis(MS). The damage it has done to his body has been so profound it renders him unable to use any form of off-the-shelf technology to communicate independently. He suffers from quadriplegia, blindness, and cannot speak clearly enough to use speech-to-text converters.  

![Miro](https://github.com/WritingTechForJarrod/app/blob/master/img/readme2.jpg?raw=true "wtfj")  
### This is Miro  
Miro is a flexible program our team is developing for our capstone engineering project, which will hopefully be useful for Jarrod and many other people with extensive and unique disabilities. Miro allows multiple inputs and outputs to be seamlessly connected to maximize the number of signals available for communication.   
  
## Design Documentation
[Design document available here](https://docs.google.com/document/d/1l9wp3MV8gngEhaP4Npji1a92KYDKru8GvrS5jWQIPqg/edit?usp=sharing "Design document")
  
## About the repo organization  
Each part of the program is designed to be run as a seperate process that communicates with other pieces through tcp/ip  
Parts of the program are compiled executables and others are python scripts  
* `bin` contains sub-folders which have precompiled windows executables and the .dlls and other resources needed to run them  
* `img` contains images used in the GUI program pieces  
* `log` contains tcp server logs and some small scripts to process data  
* `output` contains files that are generated by the user interacting with the program  
* `res` contains non-image resources, notable audio files used in common text-to-speech functions  
* `scripts` has run-time scripts that can be executed by the `System` piece to perform startup/teardown of configurations and almost any other function  
* `src` contains source files that can be run by the Runner class such as graphical user interfaces, text-to-speech converters, letter-selection state machines and other pieces of the program  
  * Inside the python source folder the `wtfj` folder contains the module classes for shared communication protocol, important classes like Piece, and utilities  
  
More details and tutorials will be coming in April 2017, for now please contact max.prokopenko _at_ gmail.com with any questions.  
