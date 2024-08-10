import datetime
import pytz
import salat
from icalendar import Calendar, Event, vRecur

# Set up calculation methods
pt = salat.PrayerTimes(salat.CalculationMethod.ISNA, salat.AsrMethod.STANDARD)

# Set location and its' timezone.
latitude = 51.8787
longitude = 0.4200
timezone = pytz.timezone('Europe/London')

# Start date and end date for the period you what salat times for.
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

# List to store prayer times
prayer_times_list = []

# Loop through each day of the year
current_date = start_date
while current_date <= end_date:
    try:
        print("working on: " + str(current_date))

        # Calculate prayer times for the current date
        prayer_times = pt.calc_times(current_date, timezone, longitude, latitude)
        
        # Store the date, prayer name, start time, and end time in a dictionary for each prayer
        prayer_names = ['fajr', 'dhuhr', 'asr', 'maghrib', 'isha']
        for prayer in prayer_names:
            start_time = prayer_times.get(prayer)
            
            prayer_times_list.append({
                'Date': current_date,
                'Prayer': prayer.capitalize(),  # Capitalize the prayer name for better readability
                'Start Time': start_time,
                'End Time': start_time + datetime.timedelta(minutes=5)
            })
    except ValueError as e:
        print(f"Error calculating prayer times for {current_date}: {e}")

    # Move to the next day
    current_date += datetime.timedelta(days=1)


# Create an ICS file
cal = Calendar()

for entry in prayer_times_list:
    event = Event()
    # Set event properties
    event.add('summary', entry['Prayer'])
    event.add('dtstart', entry['Start Time'])
    event.add('dtend', entry['End Time'])
    # The salat will be the same time for the same day next year so we can add annual repetition
    event.add('rrule', vRecur(freq='YEARLY', interval=1)) 
    
    cal.add_component(event)

# Write the ICS file
with open('prayer_times.ics', 'wb') as f:
    f.write(cal.to_ical())

print("ICS file 'prayer_times.ics' created successfully.")