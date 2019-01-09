from psychopy import visual, core, event, data, gui, sound #import some libraries from PsychoPy
import random

#get info about experiment
dialogue=gui.Dlg(title="Experiment Information")
#subject info
dialogue.addText('Subject Information')
dialogue.addField('Subject ID:')
dialogue.addField('Gender:')
dialogue.addField('Age:')
dialogue.show()

#create a window with black background, full screen, pixels
win = visual.Window(size=(800, 600), fullscr=True, color=[-1,-1,-1], monitor="testMonitor", units='pix')

if dialogue.OK: #experiment info collected successfully
    exp_info=dialogue.data
    subject_ID=exp_info[0]
    gender=exp_info[1]
    age=exp_info[2]
    
    #create experiment handler
    experiment=data.ExperimentHandler(name='VERBALRBsubject '+subject_ID,
             extraInfo={'gender':gender,
                        'age':age},
             dataFileName='subject'+subject_ID)
    
    #experiment instructions
    instr1=visual.TextStim(win,text='In this experiment you will be looking at various lines, and learning which category each line belongs to. There are only two categories, and each category is equally likely. Perfect performance is possible.', 
                            color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr1.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr2=visual.TextStim(win,text='For each line, please press one of two colored keys to indicate which category you think it belongs to. You will receive feedback regarding whether your response is Correct or Wrong ', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr2.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr3=visual.TextStim(win,text='For the last two Blocks of the experiment, the buttons corresponding to the categories will switch. You will be notified when this switch will occur.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr3.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr4=visual.TextStim(win,text='You will also be asked to keep track of various grids.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr4.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr5=visual.TextStim(win,text='You will respond regarding whether each grid matches the grid you saw 2 grids previously.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr5.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr6=visual.TextStim(win,text='If a grid is the SAME as 2 grids ago, press the Space key. If it is NOT THE SAME grid as the previous grid, do NOT press any keys. For these,  you will NOT receive feedback regarding accuracy.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr6.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr7=visual.TextStim(win,text='At the beginning of each new Block, you will NOT need to match back to the last grids from the preceding Block. Therefore, no response is required for the first two grids at the beginning of each new Block', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr7.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr8=visual.TextStim(win,text='At this point, please ask the experimenter any questions you may have. Once the experiment begins, you will not have an opportunity to ask questions until the end.', color=[1,1,1], height=40, wrapWidth=1000)
    space=visual.TextStim(win, text='Press any key to continue', color=[1,1,1], pos=(0, -300))
    instr8.draw()
    space.draw()
    win.flip()
    event.waitKeys()
    
    instr9=visual.TextStim(win,text='Now, please place each index finger on the colored keys, and your thumbs on the Space key. Please keep your fingers in these positions for the experiment. The experiment will now begin.', color=[1,1,1], height=40, wrapWidth=1000)
    start_space=visual.TextStim(win, text='Press a key to begin the experiment', color=[1,1,1], pos=(0, -300))
    instr9.draw()
    start_space.draw()
    win.flip()
    event.Mouse(visible=False)
    event.waitKeys()
    
    #depository of pre-set lines here -- from iilines.py
    lines=[visual.Line(win,start=(161.6,0), end=(-161.6,0), ori=-178.5),
           visual.Line(win,start=(174.3,0), end=(-174.3,0), ori=-154.5),
           visual.Line(win,start=(161.2,0), end=(-161.2,0), ori=-80.3),
           visual.Line(win,start=(164.4,0), end=(-164.4,0), ori=-96.5),
           visual.Line(win,start=(142.8,0), end=(-142.8,0), ori=-145.3),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-100.1),
           visual.Line(win,start=(182.1,0), end=(-182.1,0), ori=-171.5),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-135.4),
           visual.Line(win,start=(173.6,0), end=(-173.6,0), ori=-143.2),
           visual.Line(win,start=(168.3,0), end=(-168.3,0), ori=-93),
           visual.Line(win,start=(128,0), end=(-128,0), ori=-97.2),
           visual.Line(win,start=(186,0), end=(-186,0), ori=-162.3),
           visual.Line(win,start=(165.1,0), end=(-165.1,0), ori=-129),
           visual.Line(win,start=(150.6,0), end=(-150.6,0), ori=-139.6),
           visual.Line(win,start=(149.2,0), end=(-149.2,0), ori=-136.8),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-130.5),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-101.5),
           visual.Line(win,start=(172.9,0), end=(-172.9,0), ori=-141.8),
           visual.Line(win,start=(154.1,0), end=(-154.1,0), ori=-105.7),
           visual.Line(win,start=(120.9,0), end=(-120.9,0), ori=-101.5),
           visual.Line(win,start=(130.1,0), end=(-130.1,0), ori=-117),
           visual.Line(win,start=(174.3,0), end=(-174.3,0), ori=-116.3),
           visual.Line(win,start=(161.6,0), end=(-161.6,0), ori=-110.7),
           visual.Line(win,start=(167.2,0), end=(-167.2,0), ori=-182.8),
           visual.Line(win,start=(133.6,0), end=(-133.6,0), ori=-76),
           visual.Line(win,start=(160.9,0), end=(-160.9,0), ori=-99.3),#
           visual.Line(win,start=(173.2,0), end=(-173.2,0), ori=-187.7),
           visual.Line(win,start=(155.6,0), end=(-155.6,0), ori=-88.7),
           visual.Line(win,start=(179.2,0), end=(-179.2,0), ori=-181.4),
           visual.Line(win,start=(177.8,0), end=(-177.8,0), ori=-151.7),
           visual.Line(win,start=(165.8,0), end=(-165.8,0), ori=-164.4),
           visual.Line(win,start=(164.4,0), end=(-164.4,0), ori=-99.3),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-156.6),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-149.5),
           visual.Line(win,start=(158,0), end=(-158,0), ori=-86.6),
           visual.Line(win,start=(147.8,0), end=(-147.8,0), ori=-129.7),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-158),
           visual.Line(win,start=(167.6,0), end=(-167.6,0), ori=-173.6),
           visual.Line(win,start=(161.9,0), end=(-161.9,0), ori=-142.5),
           visual.Line(win,start=(147.8,0), end=(-147.8,0), ori=-64.2),
           visual.Line(win,start=(155.2,0), end=(-155.2,0), ori=-90.9),
           visual.Line(win,start=(178.2,0), end=(-178.2,0), ori=-145.3),
           visual.Line(win,start=(173.2,0), end=(-173.2,0), ori=-175),
           visual.Line(win,start=(152.4,0), end=(-152.4,0), ori=-72.5),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-94.4),
           visual.Line(win,start=(142.1,0), end=(-142.1,0), ori=-126.9),
           visual.Line(win,start=(189.1,0), end=(-189.1,0), ori=-164.4),
           visual.Line(win,start=(143.9,0), end=(-143.9,0), ori=-124.8),
           visual.Line(win,start=(148.1,0), end=(-148.1,0), ori=-93.7),#
           visual.Line(win,start=(169.7,0), end=(-169.7,0), ori=-193.4),
           visual.Line(win,start=(156.3,0), end=(-156.3,0), ori=-167.9),
           visual.Line(win,start=(159.4,0), end=(-159.4,0), ori=-92.3),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-148.1),
           visual.Line(win,start=(154.8,0), end=(-154.8,0), ori=-136.8),
           visual.Line(win,start=(141.4,0), end=(-141.4,0), ori=-107.1),
           visual.Line(win,start=(164.4,0), end=(-164.4,0), ori=-157.3),
           visual.Line(win,start=(135,0), end=(-135,0), ori=-90.2),
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-166.5),
           visual.Line(win,start=(140.7,0), end=(-140.7,0), ori=-85.9),
           visual.Line(win,start=(159.8,0), end=(-159.8,0), ori=-180.7),
           visual.Line(win,start=(175.7,0), end=(-175.7,0), ori=-112.1),
           visual.Line(win,start=(164.7,0), end=(-164.7,0), ori=-118.4),
           visual.Line(win,start=(144.9,0), end=(-144.9,0), ori=-98.6),
           visual.Line(win,start=(180.3,0), end=(-180.3,0), ori=-172.2),
           visual.Line(win,start=(172.9,0), end=(-172.9,0), ori=-123.4),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-173.6),
           visual.Line(win,start=(163.3,0), end=(-163.3,0), ori=-152.4),
           visual.Line(win,start=(179.9,0), end=(-179.9,0), ori=-164.4),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-173.6),
           visual.Line(win,start=(159.1,0), end=(-159.1,0), ori=-156.6),
           visual.Line(win,start=(172.9,0), end=(-172.9,0), ori=-201.2),
           visual.Line(win,start=(137.9,0), end=(-137.9,0), ori=-95.8),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-101.5),
           visual.Line(win,start=(179.2,0), end=(-179.2,0), ori=-191.3),
           visual.Line(win,start=(189.5,0), end=(-189.5,0), ori=-163.7),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-129),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-160.9),#
           visual.Line(win,start=(127.3,0), end=(-127.3,0), ori=-111.4),
           visual.Line(win,start=(145.7,0), end=(-145.7,0), ori=-59),
           visual.Line(win,start=(189.5,0), end=(-189.5,0), ori=-138.2),
           visual.Line(win,start=(155.9,0), end=(-155.9,0), ori=-168.6),
           visual.Line(win,start=(144.6,0), end=(-144.6,0), ori=-58.3),
           visual.Line(win,start=(182.8,0), end=(-182.8,0), ori=-151.7),
           visual.Line(win,start=(159.8,0), end=(-159.8,0), ori=-76),
           visual.Line(win,start=(160.2,0), end=(-160.2,0), ori=-117.7),
           visual.Line(win,start=(146.4,0), end=(-146.4,0), ori=-53.4),
           visual.Line(win,start=(136.8,0), end=(-136.8,0), ori=-86.6),
           visual.Line(win,start=(149.2,0), end=(-149.2,0), ori=-124.1),
           visual.Line(win,start=(177.5,0), end=(-177.5,0), ori=-139.6),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-75.3),
           visual.Line(win,start=(167.2,0), end=(-167.2,0), ori=-191.3),
           visual.Line(win,start=(165.8,0), end=(-165.8,0), ori=-126.2),
           visual.Line(win,start=(158.7,0), end=(-158.7,0), ori=-147.4),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-98.6),
           visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-95.8),
           visual.Line(win,start=(194.4,0), end=(-194.4,0), ori=-149.5),
           visual.Line(win,start=(176.8,0), end=(-176.8,0), ori=-156.6),
           visual.Line(win,start=(184.2,0), end=(-184.2,0), ori=-143.2),
           visual.Line(win,start=(152.7,0), end=(-152.7,0), ori=-148.1),
           visual.Line(win,start=(154.8,0), end=(-154.8,0), ori=-165.1),
           visual.Line(win,start=(137.2,0), end=(-137.2,0), ori=-129.7),
           visual.Line(win,start=(151.7,0), end=(-151.7,0), ori=-114.9),
           visual.Line(win,start=(141.8,0), end=(-141.8,0), ori=-97.9),
           visual.Line(win,start=(189.1,0), end=(-189.1,0), ori=-157.3),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-160.2),#
           visual.Line(win,start=(155.6,0), end=(-155.6,0), ori=-100.1),
           visual.Line(win,start=(138.9,0), end=(-138.9,0), ori=-133.3),
           visual.Line(win,start=(155.9,0), end=(-155.9,0), ori=-141.8),
           visual.Line(win,start=(127.3,0), end=(-127.3,0), ori=-105.7),
           visual.Line(win,start=(163.3,0), end=(-163.3,0), ori=-143.9),
           visual.Line(win,start=(176.8,0), end=(-176.8,0), ori=-131.2),
           visual.Line(win,start=(156.6,0), end=(-156.6,0), ori=-120.6),
           visual.Line(win,start=(178.5,0), end=(-178.5,0), ori=-150.3),
           visual.Line(win,start=(149.9,0), end=(-149.9,0), ori=-108.5),
           visual.Line(win,start=(152.7,0), end=(-152.7,0), ori=-134),
           visual.Line(win,start=(148.1,0), end=(-148.1,0), ori=-147.4),
           visual.Line(win,start=(157.7,0), end=(-157.7,0), ori=-153.8),
           visual.Line(win,start=(165.8,0), end=(-165.8,0), ori=-180),
           visual.Line(win,start=(160.9,0), end=(-160.9,0), ori=-124.8),
           visual.Line(win,start=(183.1,0), end=(-183.1,0), ori=-155.2),
           visual.Line(win,start=(141.1,0), end=(-141.1,0), ori=-89.4),
           visual.Line(win,start=(162.3,0), end=(-162.3,0), ori=-97.9),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-80.3),
           visual.Line(win,start=(139.6,0), end=(-139.6,0), ori=-117.7),
           visual.Line(win,start=(172.2,0), end=(-172.2,0), ori=-100.8),
           visual.Line(win,start=(160.2,0), end=(-160.2,0), ori=-148.8),
           visual.Line(win,start=(160.2,0), end=(-160.2,0), ori=-127.6),
           visual.Line(win,start=(153.1,0), end=(-153.1,0), ori=-144.6),#
           visual.Line(win,start=(155.2,0), end=(-155.2,0), ori=-114.9),
           visual.Line(win,start=(130.5,0), end=(-130.5,0), ori=-85.2),
           visual.Line(win,start=(135,0), end=(-135,0), ori=-83.1),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-103.6),
           visual.Line(win,start=(136.8,0), end=(-136.8,0), ori=-107.8),
           visual.Line(win,start=(186.7,0), end=(-186.7,0), ori=-169.3),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-152.4),
           visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-100.8),
           visual.Line(win,start=(175.4,0), end=(-175.4,0), ori=-143.9),
           visual.Line(win,start=(146.7,0), end=(-146.7,0), ori=-65.4),
           visual.Line(win,start=(159.1,0), end=(-159.1,0), ori=-88.7),
           visual.Line(win,start=(184.9,0), end=(-184.9,0), ori=-180),
           visual.Line(win,start=(138.2,0), end=(-138.2,0), ori=-113.5),
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-151),
           visual.Line(win,start=(170.8,0), end=(-170.8,0), ori=-150.3),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-150.3),
           visual.Line(win,start=(159.8,0), end=(-159.8,0), ori=-132.6),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-155.2),#
           visual.Line(win,start=(170.8,0), end=(-170.8,0), ori=-143.2),
           visual.Line(win,start=(151.3,0), end=(-151.3,0), ori=-101.5),
           visual.Line(win,start=(190.9,0), end=(-190.9,0), ori=-166.5),
           visual.Line(win,start=(142.1,0), end=(-142.1,0), ori=-63.3),
           visual.Line(win,start=(182.8,0), end=(-182.8,0), ori=-172.9),
           visual.Line(win,start=(124.8,0), end=(-124.8,0), ori=-92.3),#
           visual.Line(win,start=(138.6,0), end=(-138.6,0), ori=-64.7),
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-122),
           visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-139.6),
           visual.Line(win,start=(186.7,0), end=(-186.7,0), ori=-136.8),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-142.5),
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-135.4),
           visual.Line(win,start=(136.8,0), end=(-136.8,0), ori=-120.6),
           visual.Line(win,start=(160.2,0), end=(-160.2,0), ori=-114.9),
           visual.Line(win,start=(151.7,0), end=(-151.7,0), ori=-141.8),
           visual.Line(win,start=(164.7,0), end=(-164.7,0), ori=-149.5),#
           visual.Line(win,start=(187.7,0), end=(-187.7,0), ori=-174.3),
           visual.Line(win,start=(167.6,0), end=(-167.6,0), ori=-141.1),
           visual.Line(win,start=(192,0), end=(-192,0), ori=-151.7),
           visual.Line(win,start=(153.8,0), end=(-153.8,0), ori=-89.4),
           visual.Line(win,start=(168.3,0), end=(-168.3,0), ori=-124.1),
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-155.2),
           visual.Line(win,start=(129.4,0), end=(-129.4,0), ori=-111.4),
           visual.Line(win,start=(155.6,0), end=(-155.6,0), ori=-98.6),
           visual.Line(win,start=(140.4,0), end=(-140.4,0), ori=-97.9),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-148.1),
           visual.Line(win,start=(183.1,0), end=(-183.1,0), ori=-121.3),
           visual.Line(win,start=(146.4,0), end=(-146.4,0), ori=-56.2),
           visual.Line(win,start=(139.6,0), end=(-139.6,0), ori=-136.1),
           visual.Line(win,start=(179.9,0), end=(-179.9,0), ori=-160.2),
           visual.Line(win,start=(162.3,0), end=(-162.3,0), ori=-168.6),
           visual.Line(win,start=(133.6,0), end=(-133.6,0), ori=-111.4),#
           visual.Line(win,start=(156.3,0), end=(-156.3,0), ori=-169.3),
           visual.Line(win,start=(144.2,0), end=(-144.2,0), ori=-63.3),
           visual.Line(win,start=(153.1,0), end=(-153.1,0), ori=-150.3),
           visual.Line(win,start=(151.3,0), end=(-151.3,0), ori=-64.7),
           visual.Line(win,start=(142.1,0), end=(-142.1,0), ori=-105.7),
           visual.Line(win,start=(178.9,0), end=(-178.9,0), ori=-179.2),
           visual.Line(win,start=(144.9,0), end=(-144.9,0), ori=-85.9),
           visual.Line(win,start=(170.8,0), end=(-170.8,0), ori=-105),
           visual.Line(win,start=(144.9,0), end=(-144.9,0), ori=-90.2),
           visual.Line(win,start=(173.9,0), end=(-173.9,0), ori=-112.8),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-129.7),
           visual.Line(win,start=(172.9,0), end=(-172.9,0), ori=-185.6),
           visual.Line(win,start=(142.1,0), end=(-142.1,0), ori=-64.7),
           visual.Line(win,start=(135,0), end=(-135,0), ori=-112.8),
           visual.Line(win,start=(168.6,0), end=(-168.6,0), ori=-151.7),
           visual.Line(win,start=(167.9,0), end=(-167.9,0), ori=-126.2),
           visual.Line(win,start=(147.1,0), end=(-147.1,0), ori=-68.9),#
           visual.Line(win,start=(177.5,0), end=(-177.5,0), ori=-169.3),
           visual.Line(win,start=(148.8,0), end=(-148.8,0), ori=-68.2),
           visual.Line(win,start=(183.5,0), end=(-183.5,0), ori=-130.5),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-114.2),
           visual.Line(win,start=(170.4,0), end=(-170.4,0), ori=-139.6),
           visual.Line(win,start=(176.4,0), end=(-176.4,0), ori=-178.5),
           visual.Line(win,start=(137.2,0), end=(-137.2,0), ori=-81.7),
           visual.Line(win,start=(175,0), end=(-175,0), ori=-144.6),
           visual.Line(win,start=(158.7,0), end=(-158.7,0), ori=-174.3),
           visual.Line(win,start=(181.4,0), end=(-181.4,0), ori=-163),
           visual.Line(win,start=(183.5,0), end=(-183.5,0), ori=-171.5),
           visual.Line(win,start=(146.7,0), end=(-146.7,0), ori=-127.6),
           visual.Line(win,start=(128.3,0), end=(-128.3,0), ori=-92.3),
           visual.Line(win,start=(162.6,0), end=(-162.6,0), ori=-90.2),
           visual.Line(win,start=(154.1,0), end=(-154.1,0), ori=-159.4),#
           visual.Line(win,start=(141.4,0), end=(-141.4,0), ori=-117),
           visual.Line(win,start=(190.6,0), end=(-190.6,0), ori=-158.7),
           visual.Line(win,start=(168.3,0), end=(-168.3,0), ori=-115.6),
           visual.Line(win,start=(164,0), end=(-164,0), ori=-138.2),
           visual.Line(win,start=(198.3,0), end=(-198.3,0), ori=-155.9),
           visual.Line(win,start=(157.3,0), end=(-157.3,0), ori=-102.2),
           visual.Line(win,start=(144.2,0), end=(-144.2,0), ori=-77.4),
           visual.Line(win,start=(141.8,0), end=(-141.8,0), ori=-78.1),
           visual.Line(win,start=(171.1,0), end=(-171.1,0), ori=-98.6),
           visual.Line(win,start=(184.9,0), end=(-184.9,0), ori=-174.3),
           visual.Line(win,start=(161.2,0), end=(-161.2,0), ori=-177.8),
           visual.Line(win,start=(161.6,0), end=(-161.6,0), ori=-157.3),
           visual.Line(win,start=(164.7,0), end=(-164.7,0), ori=-190.6),
           visual.Line(win,start=(168.6,0), end=(-168.6,0), ori=-151.7),
           visual.Line(win,start=(180.3,0), end=(-180.3,0), ori=-125.5),
           visual.Line(win,start=(163,0), end=(-163,0), ori=-90.9),#
           visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-112.1),
           visual.Line(win,start=(162.6,0), end=(-162.6,0), ori=-179.2),
           visual.Line(win,start=(123.7,0), end=(-123.7,0), ori=-100.1),
           visual.Line(win,start=(192.3,0), end=(-192.3,0), ori=-149.5),
           visual.Line(win,start=(170.8,0), end=(-170.8,0), ori=-144.6),
           visual.Line(win,start=(191.6,0), end=(-191.6,0), ori=-143.9),
           visual.Line(win,start=(173.9,0), end=(-173.9,0), ori=-146.7),
           visual.Line(win,start=(144.9,0), end=(-144.9,0), ori=-88.7),
           visual.Line(win,start=(151,0), end=(-151,0), ori=-153.1),
           visual.Line(win,start=(166.9,0), end=(-166.9,0), ori=-169.3),
           visual.Line(win,start=(159.8,0), end=(-159.8,0), ori=-163.7),
           visual.Line(win,start=(157,0), end=(-157,0), ori=-124.1),
           visual.Line(win,start=(145.7,0), end=(-145.7,0), ori=-81.7),
           visual.Line(win,start=(153.8,0), end=(-153.8,0), ori=-120.6),
           visual.Line(win,start=(125.5,0), end=(-125.5,0), ori=-97.9),
           visual.Line(win,start=(146,0), end=(-146,0), ori=-105),#
           visual.Line(win,start=(129,0), end=(-129,0), ori=-85.2),
           visual.Line(win,start=(152,0), end=(-152,0), ori=-165.1),
           visual.Line(win,start=(134.3,0), end=(-134.3,0), ori=-117),
           visual.Line(win,start=(180.3,0), end=(-180.3,0), ori=-156.6),
           visual.Line(win,start=(136.1,0), end=(-136.1,0), ori=-113.5),
           visual.Line(win,start=(156.6,0), end=(-156.6,0), ori=-133.3),
           visual.Line(win,start=(151.3,0), end=(-151.3,0), ori=-149.5),
           visual.Line(win,start=(161.6,0), end=(-161.6,0), ori=-103.6),
           visual.Line(win,start=(123,0), end=(-123,0), ori=-104.3),
           visual.Line(win,start=(177.8,0), end=(-177.8,0), ori=-124.8),
           visual.Line(win,start=(174.3,0), end=(-174.3,0), ori=-114.9),
           visual.Line(win,start=(154.1,0), end=(-154.1,0), ori=-80.3),
           visual.Line(win,start=(131.2,0), end=(-131.2,0), ori=-95.1),#
           visual.Line(win,start=(150.6,0), end=(-150.6,0), ori=-78.8),
           visual.Line(win,start=(178.2,0), end=(-178.2,0), ori=-179.2),
           visual.Line(win,start=(124.4,0), end=(-124.4,0), ori=-95.8),
           visual.Line(win,start=(153.4,0), end=(-153.4,0), ori=-90.2),
           visual.Line(win,start=(145.7,0), end=(-145.7,0), ori=-53.4),
           visual.Line(win,start=(161.6,0), end=(-161.6,0), ori=-178.5),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-100.1),
           visual.Line(win,start=(171.8,0), end=(-171.8,0), ori=-107.1),
           visual.Line(win,start=(191.3,0), end=(-191.3,0), ori=-150.3),
           visual.Line(win,start=(163.3,0), end=(-163.3,0), ori=-177.8),
           visual.Line(win,start=(149.9,0), end=(-149.9,0), ori=-122.7),
           visual.Line(win,start=(140.4,0), end=(-140.4,0), ori=-89.4),
           visual.Line(win,start=(189.8,0), end=(-189.8,0), ori=-168.6),
           visual.Line(win,start=(170.4,0), end=(-170.4,0), ori=-149.5),
           visual.Line(win,start=(169.3,0), end=(-169.3,0), ori=-110.7),
           visual.Line(win,start=(127.3,0), end=(-127.3,0), ori=-94.4),#
           visual.Line(win,start=(141.8,0), end=(-141.8,0), ori=-116.3),
           visual.Line(win,start=(137.2,0), end=(-137.2,0), ori=-80.3),
           visual.Line(win,start=(158.4,0), end=(-158.4,0), ori=-77.4),
           visual.Line(win,start=(177.8,0), end=(-177.8,0), ori=-147.4),
           visual.Line(win,start=(145.7,0), end=(-145.7,0), ori=-115.6),
           visual.Line(win,start=(163.3,0), end=(-163.3,0), ori=-176.4),
           visual.Line(win,start=(176.8,0), end=(-176.8,0), ori=-145.3),
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-159.4),
           visual.Line(win,start=(184.5,0), end=(-184.5,0), ori=-180.7),
           visual.Line(win,start=(174.6,0), end=(-174.6,0), ori=-121.3),
           visual.Line(win,start=(146.4,0), end=(-146.4,0), ori=-146.7),
           visual.Line(win,start=(162.6,0), end=(-162.6,0), ori=-142.5),
           visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-82.4),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-144.6),
           visual.Line(win,start=(138.9,0), end=(-138.9,0), ori=-109.2),#
           visual.Line(win,start=(170.4,0), end=(-170.4,0), ori=-124.1),
           visual.Line(win,start=(144.2,0), end=(-144.2,0), ori=-105.7),
           visual.Line(win,start=(148.8,0), end=(-148.8,0), ori=-62.6),
           visual.Line(win,start=(177.5,0), end=(-177.5,0), ori=-179.2),
           visual.Line(win,start=(133.3,0), end=(-133.3,0), ori=-102.2),
           visual.Line(win,start=(176.1,0), end=(-176.1,0), ori=-182.1),
           visual.Line(win,start=(180.3,0), end=(-180.3,0), ori=-190.6),
           visual.Line(win,start=(128.7,0), end=(-128.7,0), ori=-105.7),
           visual.Line(win,start=(139.3,0), end=(-139.3,0), ori=-105.7),
           visual.Line(win,start=(176.8,0), end=(-176.8,0), ori=-159.4),
           visual.Line(win,start=(131.9,0), end=(-131.9,0), ori=-105),
           visual.Line(win,start=(156.6,0), end=(-156.6,0), ori=-122),
           visual.Line(win,start=(145.3,0), end=(-145.3,0), ori=-76.7),
           visual.Line(win,start=(192,0), end=(-192,0), ori=-148.8),#end of catA
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-52.7),#cat B
           visual.Line(win,start=(223.1,0), end=(-223.1,0), ori=-56.9),
           visual.Line(win,start=(203.3,0), end=(-203.3,0), ori=-10.2),
           visual.Line(win,start=(189.1,0), end=(-189.1,0), ori=-47),
           visual.Line(win,start=(188.4,0), end=(-188.4,0), ori=-54.1),
           visual.Line(win,start=(199.7,0), end=(-199.7,0), ori=-34.3),#
           visual.Line(win,start=(217.4,0), end=(-217.4,0), ori=-100.8),
           visual.Line(win,start=(218.1,0), end=(-218.1,0), ori=-37.1),
           visual.Line(win,start=(217.4,0), end=(-217.4,0), ori=-55.5),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-33.6),
           visual.Line(win,start=(193,0), end=(-193,0), ori=-9.5),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-97.2),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-63.3),#
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-46.3),
           visual.Line(win,start=(205.8,0), end=(-205.8,0), ori=-23.7),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-36.4),
           visual.Line(win,start=(199.4,0), end=(-199.4,0), ori=-13.8),
           visual.Line(win,start=(217.8,0), end=(-217.8,0), ori=-52),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-24.4),
           visual.Line(win,start=(201.9,0), end=(-201.9,0), ori=-10.2),
           visual.Line(win,start=(178.5,0), end=(-178.5,0), ori=-20.1),
           visual.Line(win,start=(208.6,0), end=(-208.6,0), ori=-47.7),
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-39.2),
           visual.Line(win,start=(207.2,0), end=(-207.2,0), ori=-102.9),
           visual.Line(win,start=(186.3,0), end=(-186.3,0), ori=-13.1),
           visual.Line(win,start=(183.1,0), end=(-183.1,0), ori=-54.8),
           visual.Line(win,start=(217.1,0), end=(-217.1,0), ori=-100.1),
           visual.Line(win,start=(184.5,0), end=(-184.5,0), ori=-30.8),#
           visual.Line(win,start=(233.7,0), end=(-233.7,0), ori=-72.5),
           visual.Line(win,start=(211.8,0), end=(-211.8,0), ori=-83.8),
           visual.Line(win,start=(207.2,0), end=(-207.2,0), ori=-81.7),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-37.8),
           visual.Line(win,start=(203.3,0), end=(-203.3,0), ori=-88),
           visual.Line(win,start=(204.7,0), end=(-204.7,0), ori=-44.2),
           visual.Line(win,start=(187,0), end=(-187,0), ori=-28.6),
           visual.Line(win,start=(190.9,0), end=(-190.9,0), ori=-43.5),
           visual.Line(win,start=(235.8,0), end=(-235.8,0), ori=-76.7),
           visual.Line(win,start=(208.9,0), end=(-208.9,0), ori=-90.9),
           visual.Line(win,start=(212.8,0), end=(-212.8,0), ori=-40.7),
           visual.Line(win,start=(181.7,0), end=(-181.7,0), ori=-11),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-7.4),
           visual.Line(win,start=(203.3,0), end=(-203.3,0), ori=-95.1),
           visual.Line(win,start=(219.2,0), end=(-219.2,0), ori=-83.1),
           visual.Line(win,start=(172.2,0), end=(-172.2,0), ori=-32.9),
           visual.Line(win,start=(202.2,0), end=(-202.2,0), ori=-27.9),
           visual.Line(win,start=(183.8,0), end=(-183.3,0), ori=-43.5),
           visual.Line(win,start=(217.4,0), end=(-217.4,0), ori=-107.8),#
           visual.Line(win,start=(190.9,0), end=(-190.9,0), ori=-30.8),
           visual.Line(win,start=(175,0), end=(-175,0), ori=-39.9),
           visual.Line(win,start=(214.2,0), end=(-214.2,0), ori=-104.3),
           visual.Line(win,start=(215,0), end=(-215,0), ori=-50.6),
           visual.Line(win,start=(188.8,0), end=(-188.8,0), ori=-33.6),
           visual.Line(win,start=(201.9,0), end=(-201.9,0), ori=-78.1),
           visual.Line(win,start=(210.7,0), end=(-210.7,0), ori=-25.1),
           visual.Line(win,start=(183.8,0), end=(-183.3,0), ori=-22.3),#
           visual.Line(win,start=(208.9,0), end=(-208.9,0), ori=-68.2),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-9.5),
           visual.Line(win,start=(217.4,0), end=(-217.4,0), ori=-102.2),
           visual.Line(win,start=(205.4,0), end=(-205.4,0), ori=-13.1),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-92.3),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-55.5),#
           visual.Line(win,start=(203.6,0), end=(-203.6,0), ori=-40.7),
           visual.Line(win,start=(184.9,0), end=(-184.9,0), ori=-18.7),
           visual.Line(win,start=(230.2,0), end=(-230.2,0), ori=-72.5),
           visual.Line(win,start=(208.9,0), end=(-208.9,0), ori=-51.3),
           visual.Line(win,start=(232.3,0), end=(-232.3,0), ori=-73.9),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-52),
           visual.Line(win,start=(218.8,0), end=(-218.8,0), ori=-86.6),
           visual.Line(win,start=(226.6,0), end=(-226.6,0), ori=-58.3),
           visual.Line(win,start=(199.4,0), end=(-199.4,0), ori=-76),
           visual.Line(win,start=(231.6,0), end=(-231.6,0), ori=-83.8),
           visual.Line(win,start=(196.6,0), end=(-196.6,0), ori=-6.7),
           visual.Line(win,start=(205.1,0), end=(-205.1,0), ori=-25.1),
           visual.Line(win,start=(215.7,0), end=(-215.7,0), ori=-118.4),
           visual.Line(win,start=(212.8,0), end=(-212.8,0), ori=-117),
           visual.Line(win,start=(206.8,0), end=(-206.8,0), ori=-41.4),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-79.5),
           visual.Line(win,start=(169,0), end=(-169,0), ori=-27.9),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-2.5),#
           visual.Line(win,start=(211.1,0), end=(-211.1,0), ori=-95.1),
           visual.Line(win,start=(206.8,0), end=(-206.8,0), ori=-66.8),
           visual.Line(win,start=(198.3,0), end=(-198.3,0), ori=-7.4),
           visual.Line(win,start=(224.9,0), end=(-224.9,0), ori=-67.5),
           visual.Line(win,start=(194.1,0), end=(-194.1,0), ori=-7.4),
           visual.Line(win,start=(194.1,0), end=(-194.1,0), ori=-49.8),
           visual.Line(win,start=(169.3,0), end=(-169.3,0), ori=-7.4),
           visual.Line(win,start=(203.3,0), end=(-203.3,0), ori=-10.2),
           visual.Line(win,start=(204.7,0), end=(-204.7,0), ori=-13.1),#
           visual.Line(win,start=(205.8,0), end=(-205.8,0), ori=-83.1),
           visual.Line(win,start=(178.8,0), end=(-178.8,0), ori=-16.6),#
           visual.Line(win,start=(225.6,0), end=(-225.6,0), ori=-74.6),
           visual.Line(win,start=(193.7,0), end=(-193.7,0), ori=-70.4),
           visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-37.8),
           visual.Line(win,start=(196.6,0), end=(-196.6,0), ori=-39.2),
           visual.Line(win,start=(184.2,0), end=(-184.2,0), ori=-24.4),
           visual.Line(win,start=(229.8,0), end=(-229.8,0), ori=-78.8),
           visual.Line(win,start=(213.9,0), end=(-213.9,0), ori=-82.4),
           visual.Line(win,start=(206.1,0), end=(-206.1,0), ori=-99.3),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-45.6),
           visual.Line(win,start=(213.9,0), end=(-213.9,0), ori=-47),
           visual.Line(win,start=(189.8,0), end=(-189.8,0), ori=-24.4),
           visual.Line(win,start=(202.2,0), end=(-202.2,0), ori=-13.8),
           visual.Line(win,start=(178.2,0), end=(-178.2,0), ori=-25.1),#
           visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-110.7),
           visual.Line(win,start=(216,0), end=(-216,0), ori=-117.7),
           visual.Line(win,start=(188.4,0), end=(-188.4,0), ori=-34.3),
           visual.Line(win,start=(199.4,0), end=(-199.4,0), ori=-12.4),
           visual.Line(win,start=(206.1,0), end=(-206.1,0), ori=-41.4),#
           visual.Line(win,start=(186,0), end=(-186,0), ori=-2.5),
           visual.Line(win,start=(199.7,0), end=(-199.7,0), ori=-71.1),
           visual.Line(win,start=(208.2,0), end=(-208.2,0), ori=-68.2),
           visual.Line(win,start=(203.6,0), end=(-203.6,0), ori=-26.5),
           visual.Line(win,start=(211.4,0), end=(-211.4,0), ori=-84.5),
           visual.Line(win,start=(194.4,0), end=(-194.4,0), ori=-19.4),
           visual.Line(win,start=(209.6,0), end=(-209.6,0), ori=-20.5),
           visual.Line(win,start=(208.9,0), end=(-208.9,0), ori=-25.8),
           visual.Line(win,start=(215.7,0), end=(-215.7,0), ori=-37.8),
           visual.Line(win,start=(208.9,0), end=(-208.9,0), ori=-93.7),
           visual.Line(win,start=(199.4,0), end=(-199.4,0), ori=-47.7),
           visual.Line(win,start=(221,0), end=(-221,0), ori=-79.5),
           visual.Line(win,start=(177.1,0), end=(-177.1,0), ori=-17.3),
           visual.Line(win,start=(200.5,0), end=(-200.5,0), ori=-21.6),
           visual.Line(win,start=(176.8,0), end=(-176.8,0), ori=-30.8),
           visual.Line(win,start=(184.2,0), end=(-184.2,0), ori=-28.6),
           visual.Line(win,start=(195.5,0), end=(-195.5,0), ori=-54.1),
           visual.Line(win,start=(209.6,0), end=(-209.6,0), ori=-49.8),#
           visual.Line(win,start=(196.2,0), end=(-196.2,0), ori=-55.5),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-30.8),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-29.3),#
           visual.Line(win,start=(180.7,0), end=(-180.7,0), ori=-13.1),
           visual.Line(win,start=(167.2,0), end=(-167.2,0), ori=-18.7),
           visual.Line(win,start=(189.5,0), end=(-189.5,0), ori=-23.7),
           visual.Line(win,start=(183.5,0), end=(-183.5,0), ori=-14.5),
           visual.Line(win,start=(215.7,0), end=(-215.7,0), ori=-111.4),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-61.2),
           visual.Line(win,start=(193,0), end=(-193,0), ori=-23.7),
           visual.Line(win,start=(200.8,0), end=(-200.8,0), ori=-93),
           visual.Line(win,start=(190.2,0), end=(-190.2,0), ori=-60.7),
           visual.Line(win,start=(182.8,0), end=(-182.8,0), ori=-41.4),
           visual.Line(win,start=(223.1,0), end=(-223.1,0), ori=-103.6),
           visual.Line(win,start=(177.5,0), end=(-177.5,0), ori=-35),
           visual.Line(win,start=(231.6,0), end=(-231.6,0), ori=-82.4),
           visual.Line(win,start=(210,0), end=(-210,0), ori=-71.8),
           visual.Line(win,start=(218.1,0), end=(-218.1,0), ori=-103.6),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-49.1),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-56.2),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-76.7),
           visual.Line(win,start=(196.2,0), end=(-196.2,0), ori=-11.7),
           visual.Line(win,start=(231.6,0), end=(-231.6,0), ori=-85.2),
           visual.Line(win,start=(167.9,0), end=(-167.9,0), ori=-11.7),
           visual.Line(win,start=(212.8,0), end=(-212.8,0), ori=-112.8),
           visual.Line(win,start=(196.9,0), end=(-196.9,0), ori=-4.6),#
           visual.Line(win,start=(179.6,0), end=(-179.6,0), ori=-11),
           visual.Line(win,start=(196.6,0), end=(-196.6,0), ori=-13.8),
           visual.Line(win,start=(204.7,0), end=(-204.7,0), ori=-51.3),
           visual.Line(win,start=(216.4,0), end=(-216.4,0), ori=-77.4),
           visual.Line(win,start=(200.1,0), end=(-200.1,0), ori=-46.3),
           visual.Line(win,start=(224.9,0), end=(-224.9,0), ori=-56.2),
           visual.Line(win,start=(184.9,0), end=(-184.9,0), ori=-24.4),
           visual.Line(win,start=(206.8,0), end=(-206.8,0), ori=-21.6),
           visual.Line(win,start=(206.8,0), end=(-206.8,0), ori=-31.5),
           visual.Line(win,start=(213.2,0), end=(-213.2,0), ori=-52.7),
           visual.Line(win,start=(228.4,0), end=(-228.4,0), ori=-93),
           visual.Line(win,start=(205.4,0), end=(-205.4,0), ori=-65.4),
           visual.Line(win,start=(225.6,0), end=(-225.6,0), ori=-84.5),
           visual.Line(win,start=(181.7,0), end=(-181.7,0), ori=-33.6),
           visual.Line(win,start=(198.7,0), end=(-198.7,0), ori=-63.3),
           visual.Line(win,start=(230.9,0), end=(-230.9,0), ori=-88),
           visual.Line(win,start=(179.9,0), end=(-179.9,0), ori=-10.2),
           visual.Line(win,start=(181.4,0), end=(-181.4,0), ori=-47),
           visual.Line(win,start=(186,0), end=(-186,0), ori=-6.7),
           visual.Line(win,start=(223.1,0), end=(-223.1,0), ori=-92.3),
           visual.Line(win,start=(220.3,0), end=(-220.3,0), ori=-47),
           visual.Line(win,start=(183.8,0), end=(-183.8,0), ori=-9.5),
           visual.Line(win,start=(188.4,0), end=(-188.4,0), ori=-38.5),#
           visual.Line(win,start=(207.9,0), end=(-207.9,0), ori=-104.3),
           visual.Line(win,start=(206.8,0), end=(-206.8,0), ori=-79.5),
           visual.Line(win,start=(204.7,0), end=(-204.7,0), ori=-11.7),
           visual.Line(win,start=(217.4,0), end=(-217.4,0), ori=-47),#
           visual.Line(win,start=(171.1,0), end=(-171.1,0), ori=-9.5),
           visual.Line(win,start=(200.1,0), end=(-200.1,0), ori=-56.2),
           visual.Line(win,start=(176.4,0), end=(-176.4,0), ori=-14.5),
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-19.4),
           visual.Line(win,start=(212.1,0), end=(-212.1,0), ori=-112.8),
           visual.Line(win,start=(171.8,0), end=(-171.8,0), ori=-32.2),
           visual.Line(win,start=(191.3,0), end=(-191.3,0), ori=-64),
           visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-5.3),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-71.1),
           visual.Line(win,start=(221,0), end=(-221,0), ori=-52.7),
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-94.4),
           visual.Line(win,start=(182.8,0), end=(-182.8,0), ori=-11.7),#
           visual.Line(win,start=(200.5,0), end=(-200.5,0), ori=-10.2),
           visual.Line(win,start=(207.2,0), end=(-207.2,0), ori=-74.6),
           visual.Line(win,start=(212.8,0), end=(-212.8,0), ori=-36.4),
           visual.Line(win,start=(177.1,0), end=(-177.1,0), ori=-8.8),
           visual.Line(win,start=(214.2,0), end=(-214.2,0), ori=-95.8),
           visual.Line(win,start=(197.6,0), end=(-197.6,0), ori=-13.1),
           visual.Line(win,start=(207.2,0), end=(-207.2,0), ori=-83.1),
           visual.Line(win,start=(192.3,0), end=(-192.3,0), ori=-43.5),
           visual.Line(win,start=(205.1,0), end=(-205.1,0), ori=-70.4),
           visual.Line(win,start=(218.8,0), end=(-218.8,0), ori=-93.7),
           visual.Line(win,start=(201.9,0), end=(-201.9,0), ori=-8.8),
           visual.Line(win,start=(215.3,0), end=(-215.3,0), ori=-64),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-83.8),
           visual.Line(win,start=(228,0), end=(-228,0), ori=-69.6),
           visual.Line(win,start=(215.7,0), end=(-215.7,0), ori=-107.1),#
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-50.6),
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-11),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-19.4),#
           visual.Line(win,start=(194.1,0), end=(-194.1,0), ori=-79.5),
           visual.Line(win,start=(186,0), end=(-186,0), ori=-27.9),
           visual.Line(win,start=(229.8,0), end=(-229.8,0), ori=-80.3),
           visual.Line(win,start=(192,0), end=(-192,0), ori=-68.2),
           visual.Line(win,start=(194.1,0), end=(-194.1,0), ori=-78.1),
           visual.Line(win,start=(234.4,0), end=(-234.4,0), ori=-83.8),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-52),
           visual.Line(win,start=(176.4,0), end=(-176.4,0), ori=-13.1),#
           visual.Line(win,start=(173.9,0), end=(-173.9,0), ori=-13.8),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-50.6),
           visual.Line(win,start=(233,0), end=(-233,0), ori=-78.1),
           visual.Line(win,start=(216,0), end=(-216,0), ori=-68.2),
           visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-65.4),
           visual.Line(win,start=(209.6,0), end=(-209.6,0), ori=-100.8),
           visual.Line(win,start=(218.8,0), end=(-218.8,0), ori=-51.3),
           visual.Line(win,start=(215.3,0), end=(-215.3,0), ori=-55.5),
           visual.Line(win,start=(184.9,0), end=(-184.9,0), ori=-47),
           visual.Line(win,start=(191.6,0), end=(-191.6,0), ori=-13.8),
           visual.Line(win,start=(218.1,0), end=(-218.1,0), ori=-68.2),
           visual.Line(win,start=(198,0), end=(-198,0), ori=-8.1),
           visual.Line(win,start=(228.7,0), end=(-228.7,0), ori=-76.7),
           visual.Line(win,start=(201.2,0), end=(-201.2,0), ori=-83.8),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-78.1),
           visual.Line(win,start=(207.9,0), end=(-207.9,0), ori=-78.8),#
           visual.Line(win,start=(190.2,0), end=(-190.2,0), ori=-12.4),
           visual.Line(win,start=(212.8,0), end=(-212.8,0), ori=-29.3),
           visual.Line(win,start=(223.1,0), end=(-223.1,0), ori=-56.9),
           visual.Line(win,start=(204,0), end=(-204,0), ori=-75.3),
           visual.Line(win,start=(196.9,0), end=(-196.9,0), ori=-44.2),
           visual.Line(win,start=(185.3,0), end=(-185.3,0), ori=-2.5),
           visual.Line(win,start=(190.6,0), end=(-190.6,0), ori=-47),
           visual.Line(win,start=(197.3,0), end=(-197.3,0), ori=-11),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-6.7),#
           visual.Line(win,start=(190.6,0), end=(-190.6,0), ori=-4.6),
           visual.Line(win,start=(214.2,0), end=(-214.2,0), ori=-40.7),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-9.5),
           visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-68.2),#
           visual.Line(win,start=(195.5,0), end=(-195.5,0), ori=-8.8),
           visual.Line(win,start=(201.2,0), end=(-201.2,0), ori=-44.2),
           visual.Line(win,start=(210.4,0), end=(-210.4,0), ori=-31.5),
           visual.Line(win,start=(188.4,0), end=(-188.4,0), ori=-49.8),
           visual.Line(win,start=(204.7,0), end=(-204.7,0), ori=-11.7),
           visual.Line(win,start=(214.6,0), end=(-214.6,0), ori=-51.3),
           visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-50.6),
           visual.Line(win,start=(196.2,0), end=(-196.2,0), ori=-10.2),
           visual.Line(win,start=(182.4,0), end=(-182.4,0), ori=-6.7),
           visual.Line(win,start=(175.7,0), end=(-175.7,0), ori=-28.6),#
           visual.Line(win,start=(231.9,0), end=(-231.9,0), ori=-71.8),
           visual.Line(win,start=(174.3,0), end=(-174.3,0), ori=-10.2),
           visual.Line(win,start=(190.6,0), end=(-190.6,0), ori=-15.9),
           visual.Line(win,start=(164.4,0), end=(-164.4,0), ori=-15.9),
           visual.Line(win,start=(222.4,0), end=(-222.4,0), ori=-56.9),
           visual.Line(win,start=(195.9,0), end=(-195.9,0), ori=-46.3),
           visual.Line(win,start=(201.2,0), end=(-201.2,0), ori=-48.4),
           visual.Line(win,start=(229.8,0), end=(-229.8,0), ori=-73.2),
           visual.Line(win,start=(206.1,0), end=(-206.1,0), ori=-92.3),
           visual.Line(win,start=(187.4,0), end=(-187.4,0), ori=-47.7),
           visual.Line(win,start=(179.2,0), end=(-179.2,0), ori=-11.7),#
           visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-111),
           visual.Line(win,start=(199.7,0), end=(-199.7,0), ori=-90),
           visual.Line(win,start=(195.2,0), end=(-195.2,0), ori=-59),#
           visual.Line(win,start=(167.6,0), end=(-167.6,0), ori=-13),
           visual.Line(win,start=(196.9,0), end=(-196.9,0), ori=-6),
           visual.Line(win,start=(187,0), end=(-187,0), ori=-8),
           visual.Line(win,start=(192.7,0), end=(-192.7,0), ori=-8),
           visual.Line(win,start=(213.2,0), end=(-213.2,0), ori=-76),
           visual.Line(win,start=(194.4,0), end=(-194.4,0), ori=-18),
           visual.Line(win,start=(213.2,0), end=(-213.2,0), ori=-76),
           visual.Line(win,start=(202.9,0), end=(-202.9,0), ori=-93),#
           visual.Line(win,start=(232.6,0), end=(-232.6,0), ori=-64),#
           visual.Line(win,start=(225.9,0), end=(-225.9,0), ori=-97),
           visual.Line(win,start=(202.6,0), end=(-202.6,0), ori=-65),
           visual.Line(win,start=(202.6,0), end=(-202.6,0), ori=-34),
           visual.Line(win,start=(202.9,0), end=(-202.9,0), ori=-61),
           visual.Line(win,start=(193,0), end=(-193,0), ori=-9),
           visual.Line(win,start=(222.4,0), end=(-222.4,0), ori=-89),
           visual.Line(win,start=(182.8,0), end=(-182.8,0), ori=-21),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-75),
           visual.Line(win,start=(182.1,0), end=(-182.1,0), ori=-30),
           visual.Line(win,start=(184.5,0), end=(-184.5,0), ori=-5),
           visual.Line(win,start=(210.7,0), end=(-210.7,0), ori=-112),
           visual.Line(win,start=(187.7,0), end=(-187.7,0), ori=-7),
           visual.Line(win,start=(225.9,0), end=(-225.9,0), ori=-82),
           visual.Line(win,start=(233.7,0), end=(-233.7,0), ori=-83),
           visual.Line(win,start=(192.7,0), end=(-192.7,0), ori=-6),
           visual.Line(win,start=(178.5,0), end=(-178.5,0), ori=-27),
           visual.Line(win,start=(217.1,0), end=(-217.1,0), ori=-78),
           visual.Line(win,start=(186.3,0), end=(-186.3,0), ori=-10),
           visual.Line(win,start=(194.8,0), end=(-194.8,0), ori=-45),
           visual.Line(win,start=(200.5,0), end=(-200.5,0), ori=-8),
           visual.Line(win,start=(232.6,0), end=(-232.6,0), ori=-67)]
    
    
    #categories RB
    def cat(index):
        if index < 300: #should be 300
            return ['d']
        else:
            return ['k']
            
    fixation = visual.TextStim(win, text='+', color=[1,1,1])
    
    index=range(len(lines))
    trials=data.TrialHandler(index, 1)
    
    one=visual.Rect(win, width=1, height=1, pos=(-2,2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    two=visual.Rect(win, width=1, height=1, pos=(-1,2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    three=visual.Rect(win, width=1, height=1, pos=(0,2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    four=visual.Rect(win, width=1, height=1, pos=(1,2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    five=visual.Rect(win, width=1, height=1, pos=(2,2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    
    six=visual.Rect(win, width=1, height=1, pos=(-2,1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    seven=visual.Rect(win, width=1, height=1, pos=(-1,1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    eight=visual.Rect(win, width=1, height=1, pos=(0,1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    nine=visual.Rect(win, width=1, height=1, pos=(1,1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    ten=visual.Rect(win, width=1, height=1, pos=(2,1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    
    eleven=visual.Rect(win, width=1, height=1, pos=(-2,0), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    twelve=visual.Rect(win, width=1, height=1, pos=(-1,0), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    thirteen=visual.Rect(win, width=1, height=1, pos=(0,0), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    fourteen=visual.Rect(win, width=1, height=1, pos=(1,0), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    fifteen=visual.Rect(win, width=1, height=1, pos=(2,0), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    
    sixteen=visual.Rect(win, width=1, height=1, pos=(-2,-1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    seventeen=visual.Rect(win, width=1, height=1, pos=(-1,-1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    eighteen=visual.Rect(win, width=1, height=1, pos=(0,-1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    nineteen=visual.Rect(win, width=1, height=1, pos=(1,-1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    twenty=visual.Rect(win, width=1, height=1, pos=(2,-1), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    
    t_one=visual.Rect(win, width=1, height=1, pos=(-2,-2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    t_two=visual.Rect(win, width=1, height=1, pos=(-1,-2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    t_three=visual.Rect(win, width=1, height=1, pos=(0,-2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    t_four=visual.Rect(win, width=1, height=1, pos=(1,-2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    t_five=visual.Rect(win, width=1, height=1, pos=(2,-2), units='cm', fillColor=[1,1,1], lineColor=[-1,-1,-1])
    
    b1 = [twelve, ten, t_three, four, fifteen, eight, six, t_one, three, t_two, seventeen, fourteen, seven]
    b2 = [t_one, four, t_three, nine, fifteen, fourteen, twelve, twenty, eighteen, five, eleven, t_five, nineteen]
    b3 = [three, t_two, fourteen, t_three, t_four, fifteen, sixteen, eighteen, twenty, eleven, seven, eight, twelve]
    b4 = [two, t_two, sixteen, ten,seventeen, t_one, nineteen, four, eighteen, three, eleven, nine, fourteen]
    b5 = [t_five, eleven, seven, three, eighteen, eight, sixteen, two, six, fourteen, thirteen,one,twenty]
    b6 = [one,fourteen,twenty,three,nineteen,t_three,two,thirteen,eighteen,seven,eleven,five,t_five]
    b7 = [t_four,t_three,twenty,t_five,four,t_one,nineteen,thirteen,eighteen,sixteen,two,seven,seventeen]
    b8 = [seven,fourteen,t_four,t_one,six,t_three,three,eleven,seventeen,twelve,thirteen,ten,nineteen]
    b9 = [four,nine,twenty,t_four,seventeen,t_two,sixteen,fifteen,eleven,three,five,one,ten]
    b10 = [five,twelve,eight,t_five,one,t_one,t_three,sixteen,four,nine,six,ten,seventeen]
    b11 = [one,fifteen,t_one,eight,ten,fourteen,six,five,nine,t_five,twelve,t_four,eighteen]
    b12 = [three,fifteen,ten,eighteen,fourteen,seven,sixteen,six,seventeen,t_two,t_four,t_five,eight]
    b13 = [eleven,seventeen,fourteen,nineteen,t_four,seven,t_two,three,sixteen,thirteen,two,eight,t_one]
    b14 = [t_two,t_five,seventeen,seven,fifteen,one,twenty,ten,two,three,sixteen,eleven,nine]
    b15 = [t_two,nine,two,eighteen,three,six,four,t_three,fourteen,twenty,eleven,eight,seven]
    
    int=(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15)
    
    background=visual.Rect(win, width=2000, height=2000, fillColor=[0,0,0])
    box=visual.Rect(win, width=5, height=5, units='cm', fillColor=[-1,-1,-1], lineColor=[-1,-1,-1])
    
    i=range(len(int))
    interferences = data.TrialHandler(i, 40, method='fullRandom')
    int_order=[]
    
    experiment.addLoop(trials)
    experiment.addLoop(interferences)
    line_count = 0 #number of lines correctly categorized per block
    int_count = 0 # number of interference pairs correctly identified (as either matching or not matching) per block
    match_count=0 #number of matching interference
    match=None #whether one-back matches or not
    
    for trial in trials:
        
        if event.getKeys(keyList='1'):
            x = error
        
        
        #new block text
        num_block = (trials.thisTrialN / 50) + 1
        experiment.addData('Block Number', num_block) #add block number to sheet
        txt1='Now beginning Round '
        num_block_txt=str(num_block)
        new_block=txt1+num_block_txt
        new_block_text=visual.TextStim(win, text=new_block, color=[1,1,1], height = 50)
    
        #button switch text
        button_switch='Respond quickly and the category response buttons for the lines will now be switched.'
        button_switch_text=visual.TextStim(win, text=button_switch, color=[1,1,1], height = 40, wrapWidth=1000)
        
        fast = False
        
        if (trials.thisTrialN) % 50 == 0:
            #draw now starting block number
            new_block_text.draw()
            win.flip()
            core.wait(1)
            
            line_count = 0 #restart correct line count for each new block
            int_count = 0 #restart correct int count for each new block
            match_count = 0 #restart correct match count for each new block
            
            if trials.thisTrialN == 500: #Block 11
                #draw instructions for button switching
                button_switch_text.draw()
                win.flip()
                core.wait(3)
                experiment.addData('New instruction shown?', 'Y')
                
        if trials.thisTrialN >= 500: #Round 11 and after
            fast=True
            experiment.addData('Buttons switched?', 'Y')
        
        fixation.draw() #fixation cross
        win.flip()
        core.wait(1.25)
        
        reference = len(int_order) - 2
        
        if (trials.thisTrialN) % 50 == 0: #if first of new block
            #print(trials.thisTrialN)
            print("First of new block")
            this_int = interferences.next()
        elif (trials.thisTrialN) % 50 == 1: #if second of new block
            #print(trials.thisTrialN)
            print("Second of new block")
            this_int = interferences.next()
        else: #choose if it matches with previous one (2-back)
            if match_count < 25:
                binary = [0,1]
                if random.choice(binary)==0: #0 is match
                    match = True #match
                    match_count += 1 #number of matches
                    experiment.addData('Int Match?', 'Y')
                    print('match')
                    interferences.next()
                    this_int = int_order[reference]
                    
                else:
                    match = False
                    experiment.addData('Int Match?', 'N')
                    this_int = interferences.next()
                    while(this_int == int_order[reference]):
                        this_int=random.choice(i)
                    print('not match1')
            else:
                match = False
                experiment.addData('Int Match?', 'N')
                this_int = interferences.next()
                while(this_int == int_order[reference]):
                        this_int=random.choice(i)
                print('not match2')
        background.draw()
        box.draw()
        for y in int[this_int]:
            print(this_int) #added
            y.draw()
        int_order.append(this_int)
        print(interferences.thisN)
        win.flip()
        
        if (trials.thisTrialN) % 50 == 0:
            core.wait(1.5)
        elif (trials.thisTrialN) % 50 == 1:
            core.wait(1.5)
        else:
            int_input = event.waitKeys(maxWait=1.5)
            experiment.addData('Int Response', int_input)
            if match == True:
                #response should be space for matching
                if int_input==['space']:
                    experiment.addData('Int Correct?', 'Y')
                    int_count += 1
                else:
                    experiment.addData('Int Correct?', 'N')
            else: #if match==False
                #response should be nothing for not-matching
                if int_input==None:
                    experiment.addData('Int Correct?', 'Y')
                    int_count += 1
                else:
                    experiment.addData('Int Correct?', 'N')
        
        fixation.draw()
        win.flip()
        core.wait(1.25)
        
        lines[trial].draw()
        #print(trial)
        win.flip()
        if fast == True:
            input = event.waitKeys(1.5, keyList=['d', 'k'])
            experiment.addData('Key pressed', input)
            experiment.addData('Fast?', 'Y')
        else:
            input = event.waitKeys(5, keyList=['d', 'k'])
            experiment.addData('Key pressed', input)
        if input==None: #if no response
            experiment.addData('Correct?', 'Timed out') #edit
            if fast == True:
                go_go=visual.TextStim(win, text='Please respond within 1.5 seconds.', color=[1,1,1], height = 40)
                go_go.draw()
                win.flip()
                core.wait(1)
            else:
                go=visual.TextStim(win, text='Please respond within 5 seconds.', color=[1,1,1], height=40)
                go.draw()
                win.flip()
                core.wait(1)
            #trial discarded
        else: #if there is a response
            correct_cat=cat(trials.thisIndex)
            experiment.addData('Category', correct_cat)
            if input == correct_cat:
                if fast == True:
                    experiment.addData('Correct?', 'N')
                    wrong=visual.TextStim(win, text='Wrong', color=[1,1,1], height=50)
                    w_sound=sound.SoundPyo(value=200, secs=1)
                    wrong.draw()
                    w_sound.play()
                    win.flip()
                    core.wait(1)
                else:
                    #save the data that this was right
                    experiment.addData('Correct?', 'Y')
                    line_count += 1
                    #show correct!
                    correct=visual.TextStim(win, text='Correct', color=[1,1,1], height=50)
                    r_sound=sound.backend_pyo.SoundPyo(value=500, secs=1)
                    correct.draw()
                    r_sound.play()
                    win.flip()
                    core.wait(1)
            else:
                if fast == True:
                    experiment.addData('Correct?', 'Y')
                    line_count += 1
                    #show correct!
                    correct=visual.TextStim(win, text='Correct', color=[1,1,1], height=50)
                    r_sound=sound.backend_pyo.SoundPyo(value=500, secs=1)
                    correct.draw()
                    r_sound.play()
                    win.flip()
                    core.wait(1)
                else:
                    #show wrong
                    experiment.addData('Correct?', 'N')
                    wrong=visual.TextStim(win, text='Wrong', color=[1,1,1], height=50)
                    w_sound=sound.SoundPyo(value=200, secs=1)
                    wrong.draw()
                    w_sound.play()
                    win.flip()
                    core.wait(1)

        if (trials.thisTrialN + 1) % 50 == 0: #if the next trial is beginning of new block
            #show block accuracy
            acc_count_percent=str(line_countcount*2)+'% Lines Accurate'
            current_round_num=visual.TextStim(win, text='Block '+str((trials.thisTrialN+1)/50), color=[1,1,1], pos=(0,100), height=50)
            accu_rate_text=visual.TextStim(win, text=acc_count_percent, color=[1,1,1], height=50)
            current_round_num.draw()
            accu_rate_text.draw()
            win.flip()
            experiment.addData('Total correct', count)
            experiment.addData('Percent correct', acc_count_percent)
            core.wait(3)

        if (trials.thisTrialN+1) % 50 == 0:
            experiment.addData('Line Accuracy', line_count)
            experiment.addData('Interference Accuracy', int_count)
            experiment.addData('Matching Interferences', match_count)

        experiment.nextEntry()



    end_text=visual.TextStim(win,text='The experiment has ended. Please quietly gather your belonging and quietly exit the testing room. If you have any questions, feel free to ask the experimenter. Thank you for your participation!', color=[1,1,1], height=40)
    end_text.draw()
    win.flip()
    core.wait(10)
    
else:
    'Experiment information collection unsuccessful!'
