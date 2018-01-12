"""
    @author: isabella fontes <aisabellafontes@gmail.com>


    Constants:
    Sequence - how larger can be the sequence? - depends the user entry
    Basically, the zigzag code consists in a sequence of integer numbers
    that the difference between each element with your previous element
    is a negative or positive result.

    If those results (negative or positive) equal the previous result,
    so it's not a zigzag code.

    Like that:
    e.g : 1,7,4,9,2,5 is a zigzag code [+6,-3,+5,-7,-3] => [ +,-,+,-,+]
    e.g : 1,4,7,2,5 isn't a zigzag code [+3, +3, -5, +3] => [+,+,-,+]

"""


class ZigZag(object):

    def __init__(self, sequences=[]):
        if not sequences:
            raise AttributeError
        self.sequences = sequences
        self.size = len(sequences)
        self.zigzag = False

    '''
        Function define if sequence is zigzag code or not.
        If length of sequence is less than 3 return False
        If has no sequence return False
        If sequence has no pattern like zigzag code return False
    '''
    def is_zigzag(self):
        if not self.sequences:
            self.zigzag = False
            return self.zigzag

        if len(self.sequences) < 3:
            self.zigzag = False
            return self.zigzag

        self.zigzag = True
        last = self.size - 1
        for index, number in enumerate(self.sequences):
            if index == 0:
                continue

            current = self.sequences[index]
            before = self.sequences[index - 1]

            if index == last:
                before2 = self.sequences[index-2]
                if self.has_pattern(current, before) == self.has_pattern(before, before2):
                    self.zigzag = False
                    break
            else:
                after = self.sequences[index+1]
                if self.has_pattern(current, before) == self.has_pattern(after, current):
                    self.zigzag = False
                    break

        return self.zigzag

    @staticmethod
    def has_pattern(x=int, y=int):
        if x is None or y is None:
            return None
        if x - y > 0:
            return '+'
        else:
            return '-'


if __name__ == '__main__':
    sequence = [int(number) for number in input().split()]
    zigzag = ZigZag(sequence)
    print(zigzag.is_zigzag())
