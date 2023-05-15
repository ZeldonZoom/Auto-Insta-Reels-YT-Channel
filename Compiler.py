import moviepy.editor as m
import os
import pyttsx3
from moviepy.video.compositing.concatenate import concatenate_videoclips
import VideoScrape
import random
import itertools

eng=pyttsx3.init()


def Vid_folder_finder(folder):
    current_dir=os.getcwd()
    new_path=os.path.join(current_dir,'%s' % folder)
    vid_path=os.listdir(new_path)
    for i in range(len(vid_path)):
        vid_path[i]=os.path.join(new_path, vid_path[i])
        
    
    return vid_path


users2=VideoScrape.users


def Vid_path_lst_maker():
    Vid_lst=[]
    clip_lst=[]
    for i in users2:

        Vid_lst+=Vid_folder_finder(i)

    for i in users2:
        for j in os.listdir(i):
            print(j)
            clip_lst+=[m.VideoFileClip(r'%s'% os.path.join(os.getcwd(),i,j))]
    
    
    return clip_lst
        


def compiler(Cliplist):
    print()
    print('-------COMPILING VIDEO CLIPS-------')
    print()
    Vid=m.concatenate_videoclips((Cliplist), method='compose')
    Vid.write_videofile('output.mp4')
    deleter()
    eng.say('Successfully compiled video and deleted clips')
    eng.runAndWait()


def deleter():
    for i in users2:
        b=os.listdir(i)
        print(b)
        for j in b:
            print(j)
            os.remove(os.path.join(os.getcwd(),i,j))
            print('Successfully deleted %s'%j)
        os.rmdir(i)
        print('Successfully deleted folder %s'%i)


def intro_adder():
    intro=m.VideoFileClip(r'%s'% os.path.join(os.getcwd(),'intro.mp4'))
    output=m.VideoFileClip(r'%s'% os.path.join(os.getcwd(),'output.mp4'))
    FinalVid=concatenate_videoclips([intro,output], method='compose')
    FinalVid.write_videofile('output.mp4')



clip_lst=Vid_path_lst_maker()

random.shuffle(clip_lst)

compiler(clip_lst)