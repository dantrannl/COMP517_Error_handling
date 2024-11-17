class NotABananaError(Exception):
  def __init__(self, message="NotABanana") -> None:
    super().__init__(message)

def am_I_a_banana(string):
  try:
    if "banana" not in string:
      raise NotABananaError()
    
    if string == "banana":  # Exact match to "banana"
      return "Just a Banana"
    
    elif "banana" in string:  # If "banana" is part of the string
      return "Not just banana"
    
    else: 
      raise ValueError
    
  except NotABananaError as exception:
    print(type(exception).__name__)