import sys
import pyautogui as pt
import time
import random
import math

def type_paragraph(paragraph, min_delay=0.02, max_delay=0.15, error_chance=0.01):
    """
    Typing pargraf with human-like behavior including variable speed and typos.

    Args: 
        paragraph (str): The text to be typed
        min_delay (float): Minimum delay between characters (seconds)
        max_delay (float): Maximum delay between characters (seconds)
        error_chance (float): Probability of making a typo (0-1)
    """
    # Add a delay before starting to type
    time.sleep(random.uniform(0.5, 1.0))
    
    lines = paragraph.split('\n')
    
    for line_idx, line in enumerate(lines):
        i = 0
        while i < len(line):
            char = line[i]
            
            # For very fast mode, reduce error chance
            if min_delay < 0.02:  # If very fast
                error_chance = error_chance * 0.5  # Reduce chance of error
            
            # Check if will make a typo
            if random.random() < error_chance and i > 0:
                # Make a small typo
                wrong_char = random.choice('asdfghjkl;')
                pt.typewrite(wrong_char)
                time.sleep(random.uniform(0.05, 0.15))
                
                # Delete the wrong character
                pt.press('backspace')
                time.sleep(random.uniform(0.03, 0.08))
            
            # Type character with random delay
            pt.typewrite(char)
            
            # Delay between characters with variation
            if min_delay < 0.02:  # Very fast mode
                # For very fast mode, use very small delays
                if char in '.,!?;:':
                    delay = random.uniform(0.05, 0.1)
                elif char == ' ':
                    delay = random.uniform(0.02, 0.04)
                else:
                    delay = random.uniform(min_delay, max_delay)
            else:
                #  For normal speed
                if char in '.,!?;:':
                    # Delay more after punctuation
                    delay = random.uniform(0.2, 0.4)
                elif char == ' ':
                    # Delay after space
                    delay = random.uniform(0.05, 0.15)
                else:
                    # Delay normal
                    delay = random.uniform(min_delay, max_delay)
            
            time.sleep(delay)
            i += 1
        
        # If not the last line, press Enter
        if line_idx < len(lines) - 1:
            # Delay before pressing Enter
            if min_delay < 0.02:  # Very fast mode
                line_delay = random.uniform(0.1, 0.3)
            else:
                line_delay = random.uniform(0.3, 0.7)
            
            time.sleep(line_delay)
            pt.press('enter')
            
            # Delay after pressing Enter
            if min_delay < 0.02:  # Very fast mode
                time.sleep(random.uniform(0.2, 0.4))
            else:
                time.sleep(random.uniform(0.5, 1.0))

def get_paragraph_from_file(filename):
    """Reads paragraph from a text file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def calculate_typing_speed(wpm):
    """
    Counting typing speed (words per minute) to character delay range.

    Args:
        wpm (int): Typing speed in words per minute
    Returns:
        tuple: (min_delay, max_delay) in seconds
    """
    # Asumsi rata-rata kata = 5 karakter + 1 spasi = 6 karakter
    # WPM to characters per second: (wpm * 6) / 60
    cps = (wpm * 6) / 60  # characters per second
    avg_delay = 1 / cps  # average delay per character

    # Give variation ±30%
    min_delay = avg_delay * 0.7
    max_delay = avg_delay * 1.3
    
    return min_delay, max_delay

def main():
    try:
        print("=" * 60)
        print("PARAGRAPH TYPING SIMULATOR")
        print("=" * 60)
        print("\nChoose text source:")
        print("1. Input from keyboard")
        print("2. Read from text file")

        choice = input("\nYour choice (1/2): ").strip()

        if choice == '1':
            print("\nEnter your paragraph (press Enter twice to finish):")
            lines = []
            while True:
                line = input()
                if line == "" and len(lines) > 0:
                    # Check if two empty lines are consecutive
                    if lines[-1] == "":
                        lines.pop()  # Remove the last empty line
                        break
                lines.append(line)
            paragraph = '\n'.join(lines)
            
        elif choice == '2':
            filename = input("Enter the name of the text file (e.g., text.txt): ").strip()
            paragraph = get_paragraph_from_file(filename)
            if paragraph is None:
                return
        else:
            print("Invalid choice!")
            return
        
        if not paragraph:
            print("error: paragraph must not be empty")
            return
        
        # counting text statistics
        char_count = len(paragraph)
        word_count = len(paragraph.split())
        estimated_time_normal = word_count / 40 * 60  # Assumed as 40 WPM
        
        print("\n" + "=" * 60)
        print("TEXT STATISTICS:")
        print("=" * 60)
        print(f"Character count: {char_count}")
        print(f"Word count: {word_count}")
        print(f"Estimated time (40 WPM): {estimated_time_normal:.1f} seconds")
        print("=" * 60)

        print("\nPREVIEW TEXT (50 characters):")
        print("=" * 60)
        preview = paragraph[:50] + "..." if len(paragraph) > 50 else paragraph
        print(preview)
        print("=" * 60)

        # Speed Configuration
        print("\nCONFIGURATION KECEPATAN MENGETIK:")
        print("=" * 60)
        print("1. Slow        (20 WPM)  - Similar like manual typing by a beginner")
        print("2. Medium      (40 WPM)  - Similar like normal typing")
        print("3. Fast        (80 WPM)  - Still looks natural")
        print("4. Very Fast   (600 WPM) - 10 words/second, maximum speed")
        print("5. Custom      - Enter your own WPM")
        
        speed_choice = input("\nPilihan kecepatan (1/2/3/4/5): ").strip()
        
        if speed_choice == '1':
            min_delay, max_delay = calculate_typing_speed(20)  # 20 WPM
            error_chance = 0.02
            print(f"fast: 20 WPM (~{1/min_delay:.1f} characters/second)")
            
        elif speed_choice == '2':
            min_delay, max_delay = calculate_typing_speed(40)  # 40 WPM
            error_chance = 0.01
            print(f"fast: 40 WPM (~{1/min_delay:.1f} characters/second)")
            
        elif speed_choice == '3':
            min_delay, max_delay = calculate_typing_speed(80)  # 80 WPM
            error_chance = 0.005
            print(f"fast: 80 WPM (~{1/min_delay:.1f} characters/second)")
            
        elif speed_choice == '4':
            # 10 words/second = 600 words/minute = 600 WPM
            min_delay, max_delay = calculate_typing_speed(600)  # 600 WPM (10 words/second)
            error_chance = 0.001  # Almost no error
            print(f"fast: Very Fast (600 WPM, 10 words/second)")
            print(f"≈ {1/min_delay:.1f} characters/second")
            
            # confirm for very fast typing speed
            confirm = input("\n⚠️ WARNING: This is a very fast typing speed! Continue? (y/n): ").lower()
            if confirm != 'y':
                print(" Using default speed (medium)...")
                min_delay, max_delay = calculate_typing_speed(40)
                error_chance = 0.01
                
        elif speed_choice == '5':
            try:
                custom_wpm = int(input("Enter typing speed (WPM): ").strip())
                if custom_wpm < 1 or custom_wpm > 1000:
                    print("WPM must be between 1-1000. Using default 40 WPM.")
                    custom_wpm = 40
                min_delay, max_delay = calculate_typing_speed(custom_wpm)
                error_chance = max(0.001, 0.02 * (40 / custom_wpm))  # Adjust error chance based on speed
                print(f"fast: {custom_wpm} WPM (~{1/min_delay:.1f} characters/second)")
            except ValueError:
                print("Invalid input! Using default 40 WPM.")
                min_delay, max_delay = calculate_typing_speed(40)
                error_chance = 0.01
        else:
            print("Using default speed (medium, 40 WPM)...")
            min_delay, max_delay = calculate_typing_speed(40)
            error_chance = 0.01
        
        # count estimated time
        avg_delay = (min_delay + max_delay) / 2
        estimated_time = char_count * avg_delay
        print(f"\n⏱️ Estimated typing time: {estimated_time:.1f} seconds")
        
        repeat = input("How many times to repeat? (default: 1): ").strip()
        repeat_count = int(repeat) if repeat.isdigit() and int(repeat) > 0 else 1
        
        # count total estimated time
        total_time = estimated_time * repeat_count
        if total_time > 60:
            print(f"⏱️ Total estimated time: {total_time/60:.1f} minutes")
        else:
            print(f"⏱️ Total estimated time: {total_time:.1f} seconds")
        
        print(f"\n🚀 Typing is ready! Switch to the target application in...")
        for i in range(5, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            time.sleep(1)
        print("GO!")
        
        print("\n🎯 Starting automated typing... (Press Ctrl+C to stop)")
        
        start_time = time.time()
        
        for iteration in range(repeat_count):
            if repeat_count > 1:
                print(f"\n🔄 Iteration {iteration + 1} of {repeat_count}")
            
            type_paragraph(paragraph, min_delay, max_delay, error_chance)
            
            if iteration < repeat_count - 1:
                # Delay between iterations
                delay_between = random.uniform(1, 3) if min_delay < 0.02 else random.uniform(2, 5)
                print(f"\n⏳ Waiting {delay_between:.1f} seconds before the next iteration...")
                time.sleep(delay_between)
        
        end_time = time.time()
        actual_time = end_time - start_time
        
        print(f"\n{'='*60}")
        print("✅ Finished! SUMMARY:")
        print(f"{'='*60}")
        print(f"Number of paragraphs: {repeat_count}")
        print(f"Total characters: {char_count * repeat_count}")
        print(f"Actual time: {actual_time:.1f} seconds")
        
        if actual_time > 0:
            actual_wpm = (word_count * repeat_count) / (actual_time / 60)
            print(f"Actual speed: {actual_wpm:.1f} WPM")
            print(f"Characters per second: {(char_count * repeat_count) / actual_time:.1f}")
        
        print(f"{'='*60}")
        
    except KeyboardInterrupt:
        print("\n\n❌ Typing stopped by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure you have installed the required modules:")
        print("pip install pyautogui")

if __name__ == "__main__":
    # check if module installed
    try:
        import pyautogui
    except ImportError:
        print("Modul pyautogui belum terinstal!")
        print("Install with: pip install pyautogui")
        sys.exit(1)
    
    # Setting fail-safe untuk pyautogui
    pt.FAILSAFE = True
    pt.PAUSE = 0  # Disable default pause
    
    main()
