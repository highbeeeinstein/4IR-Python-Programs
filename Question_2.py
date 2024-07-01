class Vehicle:
   def __init__(self, n, e, f,):
      self._VehicleID = n
      self._MaxSpeed = e
      self._IncreaseAmount = f
      self._CurrentSpeed = 0
      self._HorizontalPosition = 0
   def GetCurrentSpeed(self):
      return(self._CurrentSpeed)
   def GetIncreaseAmount(self):
      return(self._IncreaseAmount)
   def GetMaxSpeed(self):
      return(self._MaxSpeed)
   def GetHorizontalPosition(self):
      return(self._HorizontalPosition)
   def SetCurrentSpeed(self, s):
      self._CurrentSpeed = s
   def SetHorizontalPosition(self, p):
      self._HorizontalPosition = p

class Helicopter(Vehicle):
   def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, 
                VerticalChangeP, MaxHeightP ):
        Vehicle().__init__( self, n, e, f)
        self._VerticalPosition = 0
        self._VerticalChange = VerticalChangeP
        self._MaxHeight = MaxHeightP
