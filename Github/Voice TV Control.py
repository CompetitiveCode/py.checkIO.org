# Answer to Voice TV Control
# https://py.checkio.org/en/mission/voice-tv-control/


class VoiceCommand:
    def __init__(self, channel):
        """
        To store the list of channels
        The length of the channels
        And as the default case, current channel is the first channel
        """
        self.ch = channel
        self.length = len(self.ch)
        self.current = self.ch[0]

    def first_channel(self):
        """
        This directly assigns the first element into current channel
        Then returns the current channel through the call
        """
        self.current = self.ch[0]
        return self.current_channel()

    def last_channel(self):
        """
        This directly assigns the last element into current channel
        """
        self.current = self.ch[self.length-1]
        return self.current_channel()

    def turn_channel(self, n):
        """
        This assigns the n-th channel,
        which would be n-1 as the list start from 0,
        rather than 1
        """
        self.current = self.ch[n-1]
        return self.current_channel()

    def next_channel(self):
        """
        This will be helpful to find the next channel,
        even when the last channel was previously held
        """
        self.current = self.ch[(self.ch.index(self.current) + 1) % self.length]
        return self.current_channel()

    def previous_channel(self):
        """
        This is to check, whether we should subtract 1 from the current index
        Or if it is a corner case, like the first element,
        then we should select the last element in the channel list
        """
        temp = self.ch.index(self.current)
        if temp == 0:
            self.current = self.ch[self.length-1]
        else:
            self.current = self.ch[temp-1]
        return self.current_channel()

    def current_channel(self):
        return self.current

    def is_exist(self, val):
        """
        If a value is passed, then we should check if it is a valid index
        Any number less than or in this case equal
        to length of array will be present in the list
        Or if a string is passed, then we need to check
        if that string is present in the channel list or not
        """
        try:
            val = int(val)
            return 'Yes' if self.length >= val else 'No'
        except ValueError:
            return 'Yes' if val in self.ch else 'No'


if __name__ == '__main__':
    """
    These "asserts" using only for self-checking
    and not necessary for auto-testing
    """

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"

    print("Coding complete? Let's try tests!")
