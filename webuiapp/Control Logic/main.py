from tv_ac_control import (
    turn_on_tv, turn_off_tv, volume_up_tv, volume_down_tv,
    turn_on_ac, turn_off_ac, temperature_up_ac, temperature_down_ac
)

def main():
    # Control the TV
    print("Turning on the TV:")
    print(turn_on_tv())

    print("\nIncreasing the TV volume:")
    print(volume_up_tv())

    print("\nTurning off the TV:")
    print(turn_off_tv())

    # Control the AC
    print("\nTurning on the AC:")
    print(turn_on_ac())

    print("\nIncreasing the AC temperature:")
    print(temperature_up_ac())

    print("\nTurning off the AC:")
    print(turn_off_ac())

if __name__ == "__main__":
    main()
