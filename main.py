import time
import datetime
import pygame

def set_alarm():
    is_running = True
    while is_running:
        try:
            alarm_time = input("Enter ur alarm time(HH:MM:SS): ")
            alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
            return alarm_time.strftime("%H:%M:%S")
        except ValueError:
            print("❌ Invalid input! Please use exactly 'hh:mm:ss' (e.g., '09:05:30' or '14:30:00')")
            print("   - Hours must be 00-23\n   - Minutes/Seconds must be 00-59\n")


def main():
      pygame.mixer.init()
      alarm_sound = "alarm.mp3"
      pygame.mixer.music.load(alarm_sound)
      alarm_time = set_alarm()
      is_running = True
      while is_running:
          time.sleep(1)
          now = datetime.datetime.now()
          now = now.strftime("%H:%M:%S")
          print(now)
          if now == alarm_time:
              pygame.mixer.music.play()
              while pygame.mixer.music.get_busy():
                  print("Wake up")
                  time.sleep(1)
              is_running = False

if __name__ == "__main__":
    main()