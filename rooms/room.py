class Room:

  def __init__(selfie, description='an empty room leading to nowhere'):
    selfie.description = description
    selfie.north = None # Some other room. Or not.
    selfie.south = None
    selfie.east  = None
    selfie.west  = None
