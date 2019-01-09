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
    
    #depository of pre-set lines here -- from RBlines.py
    lines=[visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-138),
       visual.Line(win,start=(157,0), end=(-157,0), ori=-139),
       visual.Line(win,start=(174,0), end=(-174,0), ori=-68),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-84),
       visual.Line(win,start=(138,0), end=(-138,0), ori=-88),
       visual.Line(win,start=(171,0), end=(-171,0), ori=-90),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-162),
       visual.Line(win,start=(160,0), end=(-160,0), ori=-118),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-130),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-87),
       visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-33),
       visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-161),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-108),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-95),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-91),
       visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-94),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-65),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-128),
       visual.Line(win,start=(160,0), end=(-160,0), ori=-76),
       visual.Line(win,start=(138,0), end=(-138,0), ori=-26),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-50),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-112),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-90),
       visual.Line(win,start=(142,0), end=(-142,0), ori=-149),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-26),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-81),
       visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-161),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-66),
       visual.Line(win,start=(151,0), end=(-151,0), ori=-165),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-142),
       visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-134),
       visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-86),
       visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-133),
       visual.Line(win,start=(143,0), end=(-143,0), ori=-104),
       visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-68),
       visual.Line(win,start=(147,0), end=(-147,0), ori=-84),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-171),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-143),
       visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-113),
       visual.Line(win,start=(170,0), end=(-170,0), ori=-38),
       visual.Line(win,start=(166,0), end=(-166,0), ori=-67),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-138),
       visual.Line(win,start=(149,0), end=(-149,0), ori=-152),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-50),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-89),
       visual.Line(win,start=(144,0), end=(-144,0), ori=-74),
       visual.Line(win,start=(164,0), end=(-164,0), ori=-167),
       visual.Line(win,start=(146,0), end=(-146,0), ori=-75),
       visual.Line(win,start=(160,0), end=(-160,0), ori=-59),
       visual.Line(win,start=(140,0), end=(-140,0), ori=-160),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-123),
       visual.Line(win,start=(168.5,0), end=(-168.5,0), ori=-74),
       visual.Line(win,start=(154,0), end=(-154,0), ori=-124),
       visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-99),
       visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-59),
       visual.Line(win,start=(149,0), end=(-149,0), ori=-127),
       visual.Line(win,start=(152,0), end=(-152,0), ori=-38),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-163),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-43),
       visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-137),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-111),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-100),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-58),
       visual.Line(win,start=(155,0), end=(-155,0), ori=-160),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-115),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-164),
       visual.Line(win,start=(150,0), end=(-150,0), ori=-122),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-154),
       visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-145),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-119),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-170),
       visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-46),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-91),
       visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-172),
       visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-167),
       visual.Line(win,start=(158,0), end=(-158,0), ori=-105),
       visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-133),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-42),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-31),
       visual.Line(win,start=(173.5,0), end=(-173.5,0), ori=-149),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-123),
       visual.Line(win,start=(170,0), end=(-170,0), ori=-29),
       visual.Line(win,start=(164,0), end=(-164,0), ori=-149),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-63),
       visual.Line(win,start=(160,0), end=(-160,0), ori=-93),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-28),
       visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-38),
       visual.Line(win,start=(150,0), end=(-150,0), ori=-82),
       visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-133),
       visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-38),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-155),
       visual.Line(win,start=(161,0), end=(-161,0), ori=-107),
       visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-112),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-89),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-61),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-164),
       visual.Line(win,start=(158,0), end=(-158,0), ori=-144),
       visual.Line(win,start=(168,0), end=(-168,0), ori=-145),
       visual.Line(win,start=(144,0), end=(-144,0), ori=-104),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-119),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-69),
       visual.Line(win,start=(155,0), end=(-155,0), ori=-79),
       visual.Line(win,start=(154,0), end=(-154,0), ori=-53),
       visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-162),
       visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-172),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-74),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-74),
       visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-104),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-38),
       visual.Line(win,start=(153,0), end=(-153,0), ori=-116),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-126),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-90),
       visual.Line(win,start=(161.5,0), end=(-161.5,0), ori=-142),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-72),
       visual.Line(win,start=(149,0), end=(-149,0), ori=-94),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-97),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-115),
       visual.Line(win,start=(142,0), end=(-142,0), ori=-145),
       visual.Line(win,start=(158,0), end=(-158,0), ori=-99),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-152),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-46),
       visual.Line(win,start=(168.5,0), end=(-168.5,0), ori=-82),
       visual.Line(win,start=(167.5,0), end=(-167.5,0), ori=-55),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-64),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-98),
       visual.Line(win,start=(149,0), end=(-149,0), ori=-115),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-100),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-102),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-84),
       visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-28),
       visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-33),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-68),
       visual.Line(win,start=(147,0), end=(-147,0), ori=-53),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-167),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-149),
       visual.Line(win,start=(162,0), end=(-162,0), ori=-73),
       visual.Line(win,start=(161.5,0), end=(-161.5,0), ori=-133),
       visual.Line(win,start=(169,0), end=(-169,0), ori=-37),
       visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-71),
       visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-172),
       visual.Line(win,start=(146,0), end=(-146,0), ori=-59),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-169),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-131),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-165),
       visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-103),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-108),
       visual.Line(win,start=(158.5,0), end=(-158.5,0), ori=-126),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-69),
       visual.Line(win,start=(164.5,0), end=(-164.5,0), ori=-171),
       visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-29),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-164),
       visual.Line(win,start=(144,0), end=(-144,0), ori=-25),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-25),
       visual.Line(win,start=(146,0), end=(-146,0), ori=-71),
       visual.Line(win,start=(152.5,0), end=(-152.5,0), ori=-109),
       visual.Line(win,start=(172,0), end=(-172,0), ori=-144),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-99),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-141),
       visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-62),
       visual.Line(win,start=(161,0), end=(-161,0), ori=-91),
       visual.Line(win,start=(145.5,0), end=(-145.5,0), ori=-98),
       visual.Line(win,start=(152,0), end=(-152,0), ori=-122),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-172),
       visual.Line(win,start=(157,0), end=(-157,0), ori=-120),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-162),
       visual.Line(win,start=(165.5,0), end=(-165.5,0), ori=-64),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-109),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-172),
       visual.Line(win,start=(140.5,0), end=(-140.5,0), ori=-45),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-73),
       visual.Line(win,start=(153,0), end=(-153,0), ori=-51),
       visual.Line(win,start=(174,0), end=(-174,0), ori=-164),
       visual.Line(win,start=(175,0), end=(-175,0), ori=-128),
       visual.Line(win,start=(172,0), end=(-172,0), ori=-30),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-77),
       visual.Line(win,start=(159,0), end=(-159,0), ori=-151),
       visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-132),
       visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-51),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-124),
       visual.Line(win,start=(168,0), end=(-168,0), ori=-32),
       visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-106),
       visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-43),
       visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-59),
       visual.Line(win,start=(151.5,0), end=(-151.5,0), ori=-163),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-49),
       visual.Line(win,start=(172,0), end=(-172,0), ori=-99),
       visual.Line(win,start=(159,0), end=(-159,0), ori=-52),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-109),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-133),
       visual.Line(win,start=(145,0), end=(-145,0), ori=-159),
       visual.Line(win,start=(166,0), end=(-166,0), ori=-30),
       visual.Line(win,start=(144,0), end=(-144,0), ori=-54),
       visual.Line(win,start=(154,0), end=(-154,0), ori=-129),
       visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-110),
       visual.Line(win,start=(168,0), end=(-168,0), ori=-40),
       visual.Line(win,start=(154,0), end=(-154,0), ori=-154),
       visual.Line(win,start=(169.5,0), end=(-169.5,0), ori=-42),
       visual.Line(win,start=(172,0), end=(-172,0), ori=-135),
       visual.Line(win,start=(159,0), end=(-159,0), ori=-86),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-123),
       visual.Line(win,start=(150,0), end=(-150,0), ori=-159),
       visual.Line(win,start=(156.5,0), end=(-156.5,0), ori=-35),
       visual.Line(win,start=(161,0), end=(-161,0), ori=-133),
       visual.Line(win,start=(139,0), end=(-139,0), ori=-131),
       visual.Line(win,start=(159,0), end=(-159,0), ori=-155),
       visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-164),
       visual.Line(win,start=(147,0), end=(-147,0), ori=-81),
       visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-30),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-77),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-114),
       visual.Line(win,start=(147,0), end=(-147,0), ori=-66),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-165),
       visual.Line(win,start=(166.5,0), end=(-166.5,0), ori=-103),
       visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-113),
       visual.Line(win,start=(173.5,0), end=(-173.5,0), ori=-174),
       visual.Line(win,start=(163.5,0), end=(-163.5,0), ori=-78),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-42),
       visual.Line(win,start=(161,0), end=(-161,0), ori=-39),
       visual.Line(win,start=(174.5,0), end=(-174.5,0), ori=-95),
       visual.Line(win,start=(157.5,0), end=(-157.5,0), ori=-168),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-137),
       visual.Line(win,start=(147,0), end=(-147,0), ori=-123),
       visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-151),
       visual.Line(win,start=(154,0), end=(-154,0), ori=-129),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-127),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-78),
       visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-64),
       visual.Line(win,start=(140,0), end=(-140,0), ori=-140),
       visual.Line(win,start=(140.5,0), end=(-140.5,0), ori=-29),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-161),
       visual.Line(win,start=(158,0), end=(-158,0), ori=-127),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-156),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-133),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-51),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-105),
       visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-139),
       visual.Line(win,start=(143.5,0), end=(-143.5,0), ori=-125),
       visual.Line(win,start=(155.5,0), end=(-155.5,0), ori=-93),
       visual.Line(win,start=(162.5,0), end=(-162.5,0), ori=-47),
       visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-86),
       visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-30),
       visual.Line(win,start=(154.5,0), end=(-154.5,0), ori=-64),
       visual.Line(win,start=(149.5,0), end=(-149.5,0), ori=-26),
       visual.Line(win,start=(137.5,0), end=(-137.5,0), ori=-115),
       visual.Line(win,start=(142,0), end=(-142,0), ori=-56),
       visual.Line(win,start=(160.5,0), end=(-160.5,0), ori=-149),
       visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-56),
       visual.Line(win,start=(152,0), end=(-152,0), ori=-99),
       visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-103),
       visual.Line(win,start=(166,0), end=(-166,0), ori=-85),
       visual.Line(win,start=(138.5,0), end=(-138.5,0), ori=-31),
       visual.Line(win,start=(170,0), end=(-170,0), ori=-123),
       visual.Line(win,start=(171,0), end=(-171,0), ori=-111),
       visual.Line(win,start=(169,0), end=(-169,0), ori=-58),
       visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-36),
       visual.Line(win,start=(167,0), end=(-167,0), ori=-52),
       visual.Line(win,start=(151,0), end=(-151,0), ori=-162),
       visual.Line(win,start=(142.5,0), end=(-142.5,0), ori=-27),
       visual.Line(win,start=(165,0), end=(-165,0), ori=-64),
       visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-27),
       visual.Line(win,start=(139.5,0), end=(-139.5,0), ori=-138),
       visual.Line(win,start=(172.5,0), end=(-172.5,0), ori=-93),
       visual.Line(win,start=(172,0), end=(-172,0), ori=-102),
       visual.Line(win,start=(170.5,0), end=(-170.5,0), ori=-160),
       visual.Line(win,start=(141,0), end=(-141,0), ori=-140),
       visual.Line(win,start=(151,0), end=(-151,0), ori=-82),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-45),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-171),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-130),
       visual.Line(win,start=(169,0), end=(-169,0), ori=-101),
       visual.Line(win,start=(145,0), end=(-145,0), ori=-30),
       visual.Line(win,start=(147.5,0), end=(-147.5,0), ori=-66),
       visual.Line(win,start=(157,0), end=(-157,0), ori=-34),
       visual.Line(win,start=(173,0), end=(-173,0), ori=-62),
       visual.Line(win,start=(162,0), end=(-162,0), ori=-139),
       visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-71),
       visual.Line(win,start=(141.5,0), end=(-141.5,0), ori=-139),
       visual.Line(win,start=(162,0), end=(-162,0), ori=-136),
       visual.Line(win,start=(163,0), end=(-163,0), ori=-158),
       visual.Line(win,start=(155,0), end=(-155,0), ori=-172),
       visual.Line(win,start=(169,0), end=(-169,0), ori=-116),
       visual.Line(win,start=(140,0), end=(-140,0), ori=-94),
       visual.Line(win,start=(153,0), end=(-153,0), ori=-114),
       visual.Line(win,start=(165,0), end=(-165,0), ori=-53),
       visual.Line(win,start=(175,0), end=(-175,0), ori=-161),
       visual.Line(win,start=(148,0), end=(-148,0), ori=-57),
       visual.Line(win,start=(165,0), end=(-165,0), ori=-112),
       visual.Line(win,start=(153,0), end=(-153,0), ori=-62),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-38),
       visual.Line(win,start=(150.5,0), end=(-150.5,0), ori=-161),
       visual.Line(win,start=(146.5,0), end=(-146.5,0), ori=-44),
       visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-161),
       visual.Line(win,start=(148.5,0), end=(-148.5,0), ori=-173),
       visual.Line(win,start=(142,0), end=(-142,0), ori=-40),
       visual.Line(win,start=(159.5,0), end=(-159.5,0), ori=-55),
       visual.Line(win,start=(157,0), end=(-157,0), ori=-146),
       visual.Line(win,start=(144.5,0), end=(-144.5,0), ori=-44),
       visual.Line(win,start=(156,0), end=(-156,0), ori=-91),
       visual.Line(win,start=(164,0), end=(-164,0), ori=-43),
       visual.Line(win,start=(171.5,0), end=(-171.5,0), ori=-160),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-138),#cat B
       visual.Line(win,start=(226,0), end=(-226,0), ori=-139),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-68),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-84),
       visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-88),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-90),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-162),
       visual.Line(win,start=(229.5,0), end=(-229.5,0), ori=-118),
       visual.Line(win,start=(222.5,0), end=(-222,0), ori=-130),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-87),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-33),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-161),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-108),
       visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-95),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-91),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-94),
       visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-65),
       visual.Line(win,start=(224,0), end=(-224,0), ori=-128),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-76),
       visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-26),
       visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-50),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-112),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-90),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-149),
       visual.Line(win,start=(215.5,0), end=(-215.5,0), ori=-26),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-81),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-161),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-66),
       visual.Line(win,start=(228,0), end=(-228,0), ori=-165),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-142),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-134),
       visual.Line(win,start=(213,0), end=(-213,0), ori=-86),
       visual.Line(win,start=(201,0), end=(-201,0), ori=-133),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-104),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-68),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-84),
       visual.Line(win,start=(228,0), end=(-228,0), ori=-171),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-143),
       visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-113),
       visual.Line(win,start=(213,0), end=(-213,0), ori=-38),
       visual.Line(win,start=(230,0), end=(-230,0), ori=-67),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-138),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-152),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-50),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-89),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-74),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-167),
       visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-75),
       visual.Line(win,start=(198,0), end=(-198,0), ori=-59),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-160),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-123),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-74),
       visual.Line(win,start=(203.5,0), end=(-203.5,0), ori=-124),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-99),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-59),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-127),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-38),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-163),
       visual.Line(win,start=(229,0), end=(-229,0), ori=-43),
       visual.Line(win,start=(200,0), end=(-200,0), ori=-137),
       visual.Line(win,start=(213,0), end=(-213,0), ori=-111),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-100),
       visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-58),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-160),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-115),
       visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-164),
       visual.Line(win,start=(221,0), end=(-221,0), ori=-122),
       visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-154),
       visual.Line(win,start=(228,0), end=(-228,0), ori=-145),
       visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-119),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-170),
       visual.Line(win,start=(225,0), end=(-225,0), ori=-46),
       visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-91),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-172),
       visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-167),
       visual.Line(win,start=(220,0), end=(-220,0), ori=-105),
       visual.Line(win,start=(207,0), end=(-207,0), ori=-133),
       visual.Line(win,start=(198,0), end=(-198,0), ori=-42),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-31),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-149),
       visual.Line(win,start=(211,0), end=(-211,0), ori=-123),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-29),
       visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-149),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-63),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-93),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-28),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-38),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-82),
       visual.Line(win,start=(204.5,0), end=(-204.5,0), ori=-133),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-38),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-155),
       visual.Line(win,start=(200.5,0), end=(-200.5,0), ori=-107),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-112),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-89),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-61),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-164),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-144),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-145),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-104),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-119),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-69),
       visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-79),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-53),
       visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-162),
       visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-172),
       visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-74),
       visual.Line(win,start=(225,0), end=(-225,0), ori=-74),
       visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-104),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-38),
       visual.Line(win,start=(204.5,0), end=(-204.5,0), ori=-116),
       visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-126),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-90),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-142),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-72),
       visual.Line(win,start=(229.5,0), end=(-229.5,0), ori=-94),
       visual.Line(win,start=(227,0), end=(-227,0), ori=-97),
       visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-115),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-145),
       visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-99),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-152),
       visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-46),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-82),
       visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-55),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-64),
       visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-98),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-115),
       visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-100),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-102),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-84),
       visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-28),
       visual.Line(win,start=(200,0), end=(-200,0), ori=-33),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-68),
       visual.Line(win,start=(213,0), end=(-213,0), ori=-53),
       visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-167),
       visual.Line(win,start=(228,0), end=(-228,0), ori=-149),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-73),
       visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-133),
       visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-37),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-71),
       visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-172),
       visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-59),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-169),
       visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-131),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-165),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-103),
       visual.Line(win,start=(211,0), end=(-211,0), ori=-108),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-126),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-69),
       visual.Line(win,start=(222,0), end=(-222,0), ori=-171),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-29),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-164),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-25),
       visual.Line(win,start=(211.5,0), end=(-211.5,0), ori=-25),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-71),
       visual.Line(win,start=(215,0), end=(-215,0), ori=-109),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-144),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-99),
       visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-141),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-62),
       visual.Line(win,start=(227,0), end=(-227,0), ori=-91),
       visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-98),
       visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-122),
       visual.Line(win,start=(217,0), end=(-217,0), ori=-172),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-120),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-162),
       visual.Line(win,start=(205,0), end=(-205,0), ori=-64),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-109),
       visual.Line(win,start=(220.5,0), end=(-220.5,0), ori=-172),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-45),
       visual.Line(win,start=(200,0), end=(-200,0), ori=-73),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-51),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-164),
       visual.Line(win,start=(227.5,0), end=(-227.5,0), ori=-128),
       visual.Line(win,start=(215,0), end=(-215,0), ori=-30),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-77),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-151),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-132),
       visual.Line(win,start=(229,0), end=(-229,0), ori=-51),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-124),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-32),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-106),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-43),
       visual.Line(win,start=(212.5,0), end=(-212.5,0), ori=-59),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-163),
       visual.Line(win,start=(198.5,0), end=(-198.5,0), ori=-49),
       visual.Line(win,start=(201,0), end=(-201,0), ori=-99),
       visual.Line(win,start=(229,0), end=(-229,0), ori=-52),
       visual.Line(win,start=(201,0), end=(-201,0), ori=-109),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-133),
       visual.Line(win,start=(209.5,0), end=(-209.5,0), ori=-159),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-30),
       visual.Line(win,start=(226.5,0), end=(-226.5,0), ori=-54),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-129),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-110),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-40),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-154),
       visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-42),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-135),
       visual.Line(win,start=(209,0), end=(-209,0), ori=-86),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-123),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-159),
       visual.Line(win,start=(228,0), end=(-228,0), ori=-35),
       visual.Line(win,start=(218,0), end=(-218,0), ori=-133),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-131),
       visual.Line(win,start=(225,0), end=(-225,0), ori=-155),
       visual.Line(win,start=(203,0), end=(-203,0), ori=-164),
       visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-81),
       visual.Line(win,start=(224,0), end=(-224,0), ori=-30),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-77),
       visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-114),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-66),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-165),
       visual.Line(win,start=(200,0), end=(-200,0), ori=-103),
       visual.Line(win,start=(198,0), end=(-198,0), ori=-113),
       visual.Line(win,start=(224.5,0), end=(-224.5,0), ori=-174),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-78),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-42),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-39),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-95),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-168),
       visual.Line(win,start=(217,0), end=(-217,0), ori=-137),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-123),
       visual.Line(win,start=(201,0), end=(-201,0), ori=-151),
       visual.Line(win,start=(225,0), end=(-225,0), ori=-129),
       visual.Line(win,start=(221,0), end=(-221,0), ori=-127),
       visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-78),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-64),
       visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-140),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-29),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-161),
       visual.Line(win,start=(201,0), end=(-201,0), ori=-127),
       visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-156),
       visual.Line(win,start=(207.5,0), end=(-207.5,0), ori=-133),
       visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-51),
       visual.Line(win,start=(228.5,0), end=(-228.5,0), ori=-105),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-139),
       visual.Line(win,start=(206,0), end=(-206,0), ori=-125),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-93),
       visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-47),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-86),
       visual.Line(win,start=(224,0), end=(-224,0), ori=-30),
       visual.Line(win,start=(224,0), end=(-224,0), ori=-64),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-26),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-115),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-56),
       visual.Line(win,start=(223,0), end=(-223,0), ori=-149),
       visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-56),
       visual.Line(win,start=(215,0), end=(-215,0), ori=-99),
       visual.Line(win,start=(226,0), end=(-226,0), ori=-103),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-85),
       visual.Line(win,start=(229,0), end=(-229,0), ori=-31),
       visual.Line(win,start=(222,0), end=(-222,0), ori=-123),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-111),
       visual.Line(win,start=(223.5,0), end=(-223.5,0), ori=-58),
       visual.Line(win,start=(215,0), end=(-215,0), ori=-36),
       visual.Line(win,start=(202.5,0), end=(-202.5,0), ori=-52),
       visual.Line(win,start=(227,0), end=(-227,0), ori=-162),
       visual.Line(win,start=(208,0), end=(-208,0), ori=-27),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-64),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-27),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-138),
       visual.Line(win,start=(210.5,0), end=(-210.5,0), ori=-93),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-102),
       visual.Line(win,start=(225,0), end=(-225,0), ori=-160),
       visual.Line(win,start=(201.5,0), end=(-201.5,0), ori=-140),
       visual.Line(win,start=(204,0), end=(-204,0), ori=-82),
       visual.Line(win,start=(211,0), end=(-211,0), ori=-45),
       visual.Line(win,start=(203.5,0), end=(-203.5,0), ori=-171),
       visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-130),
       visual.Line(win,start=(205.5,0), end=(-205.5,0), ori=-101),
       visual.Line(win,start=(202,0), end=(-202,0), ori=-30),
       visual.Line(win,start=(225.5,0), end=(-225.5,0), ori=-66),
       visual.Line(win,start=(217.5,0), end=(-217.5,0), ori=-34),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-62),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-139),
       visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-71),
       visual.Line(win,start=(212,0), end=(-212,0), ori=-139),
       visual.Line(win,start=(199,0), end=(-199,0), ori=-136),
       visual.Line(win,start=(230,0), end=(-230,0), ori=-158),
       visual.Line(win,start=(213.5,0), end=(-213.5,0), ori=-172),
       visual.Line(win,start=(208.5,0), end=(-208.5,0), ori=-116),
       visual.Line(win,start=(219.5,0), end=(-219.5,0), ori=-94),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-114),
       visual.Line(win,start=(221.5,0), end=(-221.5,0), ori=-53),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-161),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-57),
       visual.Line(win,start=(199.5,0), end=(-199.5,0), ori=-112),
       visual.Line(win,start=(206.5,0), end=(-206.5,0), ori=-62),
       visual.Line(win,start=(217,0), end=(-217,0), ori=-38),
       visual.Line(win,start=(197.5,0), end=(-197.5,0), ori=-161),
       visual.Line(win,start=(218.5,0), end=(-218.5,0), ori=-44),
       visual.Line(win,start=(219,0), end=(-219,0), ori=-161),
       visual.Line(win,start=(224,0), end=(-224,0), ori=-173),
       visual.Line(win,start=(222.5,0), end=(-222.5,0), ori=-40),
       visual.Line(win,start=(205,0), end=(-205,0), ori=-55),
       visual.Line(win,start=(214,0), end=(-214,0), ori=-146),
       visual.Line(win,start=(216.5,0), end=(-216.5,0), ori=-44),
       visual.Line(win,start=(210,0), end=(-210,0), ori=-91),
       visual.Line(win,start=(227,0), end=(-227,0), ori=-43),
       visual.Line(win,start=(229,0), end=(-229,0), ori=-160)]
    
    
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
