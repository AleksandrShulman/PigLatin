import unittest
from PigLatin import PigLatin

class PigLatinTranslationTest(unittest.TestCase):
  """
  Class to verify that translation occur properly.

  Places where testing and implementation are known to be deficient:
  TODO: Test capitalization preservation more thoroughly. First word capitalization is an expected bug.
        Proper name capitalization is also an issue
  TODO: Test apostrophes (e.g. it's)
  TODO: Test single characters (e.g. "a")
  TODO: Test combinations of the above ("It's Mike's")
  TODO: Test with formatted text (e.g. paragraphs)
  """
  def test_constant_words(self):
    """
    Verify that words that begin with constants are translated properly
    """
    input_list = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove']
    output_list = ['igpay', 'ananabay', 'ashtray', 'appyhay', 'uckday', 'oveglay']

    self._compare_input_output_lists(input_list, output_list)

  def test_voweled_words(self):
    """
    Verify that words that begin with vowels are translated properly
    """
    input_list = ['eat', 'omelet', 'are']
    output_list = ['eatyay', 'omeletyay', 'areyay']

    self._compare_input_output_lists(input_list, output_list)

  def test_simple_sentences(self):
    """
    Test a few sentences to see how punction is handled.
    """
    input_list = ["Hi my name is Aleks", "Hi my name is Aleks!"]
    output_list = ["iHay ymay amenay isyay Aleksyay",
                   "iHay ymay amenay isyay Aleksyay!"]

    self._compare_input_output_lists(input_list, output_list)

  def test_simple_sentence_with_punction(self):
    text = "hi my name is Aleks!"
    print PigLatin.translate(text)

  def test_y_as_vowel(self):
    """
    y should be a vowel if no other vowels are found
    """
    input_list = ['my', 'buy']
    output_list = ['ymay', 'uybay']
    self._compare_input_output_lists(input_list, output_list)

  @unittest.skip("Correct behavior not yet implemented")
  def test_single_characters(self):
    """ Verify that words with apostrophes work well.
    #TODO: Actually implement
    """
    input_list = ["A house", "What a house", "I have a house", "He has a house"]
    output_list = ["Ayay ousehay", "Atwhay ayay ousehay",
                   "Iyay avehay ayay ousehay", "Ehay ashay ayay ousehay"]
    self._compare_input_output_lists(input_list, output_list)

  @unittest.skip("Correct behavior not yet implemented")
  def test_words_with_apostrophe(self):
    """
    Verify that words with apostrophes work well.
    #TODO: Actually implement
    """
    input_list = ["it's", "let's", "Mark's"]
    output_list = ["itsyay", "etslay", "Mark's"]

    self._compare_input_output_lists(input_list, output_list)

  def _compare_input_output_lists(self, input_list, output_list):
    for i in range(0, len(input_list)):
      result = PigLatin.translate(input_list[i])
      self.assertEquals(result, output_list[i])

if __name__ == '__main__':
    unittest.main()