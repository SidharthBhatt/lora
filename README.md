Intro: 
Ever gone camping and wondered what animals were around you? Limited cell service, SD cards are too time intensive, and wifi's range is too limited. Introducing a custom trail camera featuring a lora rasberry pi hat PCB and worlds first open source lora video streaming protocol written in python. I literally wrote the code so an image can be converted into bytes, turned into radio frequencies, and subsequently decoded up to 2 miles away. Images take less than a minute to be sent and can be sorted with a modified version of PyTorch Wildlife. 

Motivation: 
Really wanted to do a big project (after doing many small ones) and this one was accessible, interesting, and made the world a better place. I took a prototype of this on Hackclub's the trail.

Challenges:
- didn't know what a pcb was -> learned how to use easyeda
- first pcb had the wrong ipex connector -> bought new ipex connector
- first pcb's moduels came dead on arrival -> created second pcb
- second pcb had a component in the wrong orientation -> individually desodered a 40 pin header, broke it, and resodered only the metal bits that were needed
- webcam drivers weren't working -> used ffmpeg
- base64 encoding wasn't working -> used pil library
- some packets were being missed  -> increased wait time between packets

How it works: 
![image](https://github.com/user-attachments/assets/f6232446-1c0b-4e67-a044-f8bd973873ba)

![image](https://github.com/user-attachments/assets/9380932b-402d-43e7-a354-f009e1f05b4b)

![image](https://github.com/user-attachments/assets/5b674318-ba81-40cc-a534-95e72daca2bd)


# PCB ✔

I created a PCB that easily connects a lora module with a sx1278 chip to a rasberry pi 3. This is much better than the jumper wires I prototyped because its much more portable. 
![image](https://github.com/SidharthBhatt/lora/assets/81537231/c85af4df-c06c-4aa9-a73f-0e79b648be90)



