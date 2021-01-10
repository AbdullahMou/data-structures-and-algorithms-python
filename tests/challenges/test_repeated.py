from data_structures_and_algorithms.challenges.repeated_word.repeated_word import *

def test_string():
    string = 'It  was a queer, sultry summer, the summer they electrocuted the Rosenbergs,'
    assert repeared_word(string) == 'summer'

def test_string1():
    string = 'Once upon a time, there was a brave princess who'
    assert repeared_word(string) == 'a'

def test_string2():
    string = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it'
    assert repeared_word(string) =='it'
