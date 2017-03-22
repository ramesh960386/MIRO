from wtfj import *
import random
import time
random.seed()


class Blink(Piece):

	def _AFTER_start(self):
		self._time_last_eye_msg_recvd = None
		self._blinked = False
		self._blink_threshold = .2
		self._select_val = 0

	def _ON_eyetracker_gaze(self,data):
		# Blink module only needs to detect blink (based on time without coords)
		self._time_last_eye_msg_recvd = time.clock()

	def _DURING_poll(self):
		if self._time_last_eye_msg_recvd is not None:
			now = time.clock()
			delta = now - self._time_last_eye_msg_recvd
			if delta > self._blink_threshold:
				if self._blinked is False:
					self._blinked = True
					self.send(Msg.SELECT)
			else:
				self._blinked = False

	@staticmethod
	def script():

		eyes = [
			'@blink marco',
			'@blink period 0.1',
			'@blink uptime'
		]

		for i in range(0,5):
			x,y = random.randint(0,1280),random.randint(0,720)
			msg = 'eyetracker gaze '+str(x)+','+str(y)
			eyes.append(msg)

		eyes.append('@blink period 1')

		for i in range(0,5):
			x,y = random.randint(0,1280),random.randint(0,720)
			msg = 'eyetracker gaze '+str(x)+','+str(y)
			eyes.append(msg)
			eyes.append(pack(Uid.SYSTEM,Msg.IDLE,None))

		eyes.append('@blink period 0.1')

		for i in range(0,5):
			x,y = random.randint(0,1280),random.randint(0,720)
			msg = 'eyetracker gaze '+str(x)+','+str(y)
			eyes.append(msg)

		eyes.append('@blink stop')

		return Script(eyes)


if __name__ == '__main__':
	from sys import argv
	Runner.run_w_cmd_args(Blink,argv,subscriptions=['eyetracker'])