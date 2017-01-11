import re

class PigLatin(object):
  """
  The kernel of the application. This will do the heavy lifting when it comes to
  the translation of words and phrases
  """

  VOWELS = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}

  def __init__(self):
    pass

  @staticmethod
  def translate(input):
    """
    Translate the input from English into PigLatin
    :param input: a string containing any amount of PigLatin text.
    :return: a string containing the same text translated into PigLatin.
    """
    if not input:
      '''
      Null or empty strings represent bad input. We will throw an exception
      and the app container will catch it, deal with it, and return
      appropriate 4xx error code to the user.
      '''
      raise Exception("Input needs to not be empty")

   # General strategy: Create a regex that matches words. Replace a word with
   # its translated equivalent.
    words_to_replace = list([x for x in set(re.split("[\t\n\s:/,.;!?:&-]", input)) if len(x)>0 ])
    for word in words_to_replace:
      input = input.replace(word, PigLatin.translate_word(word), 1)

    return input

  @staticmethod
  def translate_word(word):
    """
    Given an input word, produce the PigLatin equivalent.
    Making a judgement call where in the absense of other vowels, 'y' is
    now considered a vowel.
    :param word: a string
    :return: string - the word in PigLatin
    """
    if PigLatin.begins_with_vowel(word):
      # Rule is to add "yay" to anything that begins with a vowel
      return word + "yay"
    else:
      # Rule is take anything before the first vowel is placed at the end of the word.
      # Then, "ay" is added.
      split_word = re.split('[aeiouAEIOU]', word, 1)

      if len(split_word) == 1:
        # There were no matches so now we should include yY
        split_word = re.split('[aeiouyAEIOUY]', word, 1)

      first_constants = split_word[0]
      word = word.replace(first_constants, '', 1)
      resulting_word = word + first_constants + "ay"
      return resulting_word
    pass

  @staticmethod
  def begins_with_vowel(word):
    """
    Given a word, this will tell us if it's a vowel or a silent letter
    :param word: a word to examine
    :return: Whether it starts with a vowel
    """
    if word[0] in PigLatin.VOWELS:
      return True
    return False

if __name__ == "__main__":
  pass