class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]

        def solved(index: int, led_used: int, hr: int, minutes: int):
            if hr > 11 or minutes > 59:
                return
            if led_used == turnedOn:
                result.append(f"{hr}:{minutes:02d}")
                return
            if index == 10:
                return
            if index < 4:
                solved(
                    index=index + 1, led_used=led_used + 1, hr=hr + leds[index], minutes=minutes
                )
            else:
                solved(index=index + 1, led_used=led_used + 1, hr=hr, minutes=minutes+leds[index])
            solved(index=index + 1, led_used=led_used, hr=hr, minutes=minutes)

        solved(index=0, led_used=0, hr=0, minutes=0)
        return result
