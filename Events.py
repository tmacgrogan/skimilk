class Trigger:
    def __init__(self):
        self.__listeners = []

    def addListener(self, listener):
        self.__listeners.append(listener)
    
    def notifyListeners(self, *args, **kwargs):
        for listener in self.__listeners:
            listener.notify(self, *args, **kwargs)
 
 
class Listener:
    def __init__(self, trigger):
        trigger.addListener(self)

    def notify(self, trigger, *args, **kwargs):
        print('Got', args, kwargs, 'From', trigger)
 
 
class MidiEvent:
	
	def __init__(self, pygEvent):
		self.channel = pygEvent.status & 15
		self.type = pygEvent.status >> 4
		self.data1, self.key, self.programNum, self.chanAftertouchPressure = pygEvent.data1
		self.data2, self.velocity, self.keyAftertouchPressure = pygEvent.data2
		self.timestamp = pygEvent.timestamp
		
		
 
MidiEventType = dict(NoteOff = 8, NoteOn = 9, KeyAftertouch = 10, ControlChange = 11, ProgramChange = 12, ChannelAftertouch = 13, Bend = 14, System = 15)