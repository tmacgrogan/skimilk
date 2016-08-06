import sys, pygame, pygame.midi, pygame.fastevent
from pygame.locals import *
from slideshow import Slideshow

def main():
    print('starting')
    pygame.init()
    pygame.midi.init()
    pygame.fastevent.init()
    
    midiInput = pygame.midi.Input(pygame.midi.get_default_input_id())
    midiOutput = pygame.midi.Output(pygame.midi.get_default_output_id())
    
    show = Slideshow('cat')
    
    going = True
    while going:
        events = pygame.fastevent.get()
        for e in events:
            if e.type in [QUIT]:
                going = False
            if e.type in [KEYDOWN]:
                going = False
            if e.type in [pygame.midi.MIDIIN]:
                print (e)
                playNote(midiOutput, e, show)
                
        if midiInput.poll():
            midi_events = midiInput.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, midiInput.device_id)

            for m_e in midi_evs:
                pygame.fastevent.post( m_e )
                
        pygame.time.wait(30)
    print('quitting')
    pygame.midi.quit()
    
on = {}   

def playNote(out, event, show):
    chan = event.status & 15
    index = (chan * 127) + event.data1
    
    if (event.status >> 4) == 144 >> 4:
        if index in on:
            out.note_off(event.data1, event.data2, chan)
            del on[index]
            show.dropSlide(index)
            print 'off ' + str(index)
        else:
            out.note_on(event.data1, event.data2, chan)
            on[index] = "on"
            show.pickSlide(index)
            print 'on ' + str(index)
    elif (event.status >> 4) == 128 >> 4:
        out.note_off(event.data1, event.data2, chan)
        del on[index]
        show.dropSlide(index)
        print 'off ' + str(index)
    elif event.status >> 4 == 192 >> 4:
        out.set_instrument(event.data1, chan)
        print 'instrument set'
    # print on
    
class Input:
    def __init__(self):
        print 'asdf'
        
class MidiInput(Input):
    def __init__(self):
        print 'asdf'
        
if __name__ == "__main__":
    main()