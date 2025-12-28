#!/usr/bin/env python3
"""
Caffeine Calculator & Meeting Buffer
Because developers need to know when to panic-brew.
"""

import datetime
import sys

def parse_time(time_str):
    """Convert 'HH:MM' to minutes since midnight. Also accepts 'now'."""
    if time_str.lower() == 'now':
        now = datetime.datetime.now()
        return now.hour * 60 + now.minute
    try:
        hour, minute = map(int, time_str.split(':'))
        return hour * 60 + minute
    except:
        print("Time format: HH:MM or 'now'")
        sys.exit(1)

def main():
    print("☕ Caffeine Buffer 9000 ☕")
    print("Calculate your panic window between meetings\n")
    
    # Get current time or start time
    start_input = input("Meeting start time (HH:MM or 'now'): ")
    start_minutes = parse_time(start_input)
    
    # Get next meeting time
    end_input = input("Next meeting time (HH:MM): ")
    end_minutes = parse_time(end_input)
    
    # Calculate buffer
    total_buffer = end_minutes - start_minutes
    
    if total_buffer <= 0:
        print("\n⚠️  Time travel not supported. Check your times.")
        return
    
    # Coffee constants (in minutes)
    BREW_TIME = 5      # Time to make coffee
    DRINK_TIME = 10    # Time to actually enjoy it
    BRAIN_RESET = 5    # Time to remember what you were doing
    
    coffee_cycles = 0
    remaining = total_buffer
    
    print(f"\n📊 Total buffer: {total_buffer} minutes")
    
    # Calculate how many coffee breaks fit
    while remaining >= (BREW_TIME + DRINK_TIME):
        coffee_cycles += 1
        remaining -= (BREW_TIME + DRINK_TIME)
        print(f"  Coffee #{coffee_cycles}: -{BREW_TIME + DRINK_TIME} min")
        
        # Account for context switching
        if remaining >= BRAIN_RESET:
            remaining -= BRAIN_RESET
            print(f"    Brain reset: -{BRAIN_RESET} min")
    
    print(f"\n✅ You can fit {coffee_cycles} coffee break(s)")
    print(f"⏰ {remaining} minutes buffer remaining")
    
    # Safety warnings
    if coffee_cycles == 0:
        print("\n🚨 No coffee possible. Consider rescheduling life.")
    elif remaining < 5:
        print("\n⚠️  Danger zone! You'll be late for the next meeting.")
    else:
        print("\n🎉 Safe to caffeinate! (Results not guaranteed)")
    
    # Bonus: caffeine math
    if coffee_cycles > 0:
        mg_caffeine = coffee_cycles * 95
        print(f"\n⚡ Estimated caffeine: {mg_caffeine}mg")
        if mg_caffeine > 300:
            print("   (You'll be debugging at light speed)")

if __name__ == "__main__":
    main()
