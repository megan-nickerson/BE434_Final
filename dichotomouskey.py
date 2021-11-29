#!/usr/bin/env python3
"""
Author : megannickerson <megannickerson@localhost>
Date   : 2021-11-24
Purpose: Identify the Unknown Gram Positive Bacteria
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Identify the Unknown Gram Positive Bacteria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    key_start = "yes"

    while key_start == "yes":
        answer = input("Would you like to determine an unknown bacteria? (yes/no)")

        if answer.lower().strip() == "yes" or answer.lower().strip() == "y":
            answer = input("Is your bacteria Gram positive or Gram negative? (positive/negative)")
            if answer.lower().strip() == "positive" or answer.lower().strip() == "p":
                answer = input("What is the morphology of your bacteria? (Bacilli/Cocci)")
                if answer.lower().strip() == "bacilli" or answer.lower().strip() == "b":
                    answer = input("Your bacteria could be 1 of 8 in this key. What is the result of your catalase test? (positive/negative)")
                    if answer.lower().strip() == "positive" or answer.lower().strip() == "p":
                        answer = input("Your bacteria could be 1 of 6 in this key. What is the result of your SBA? (alpha/beta/double halo)")
                        if answer.lower().strip() == "alpha" or answer.lower().strip() == "beta" or answer.lower().strip() == "a" or answer.lower().strip() == 'b':
                            answer = input("Your bacteria could be 1 of 4 in this key. What is the result of your urease test? (positive/negative)")
                            if answer.lower().strip() == "positive" or answer.lower().strip() == "p":
                                answer = input("Your bacteria could be 1 of 2 bacteria in this key. What is the result of your CAMP test? (positive/negative)")
                                if answer.lower().strip() == "positive" or answer.lower().strip() == "p":
                                    answer = input("Your bacteria is Corynebacterium pseudotuberculosis!")
                                elif answer.lower().strip() == "negative" or answer.lower().strip() == "n":
                                    answer = input("Your bacteria is Mycobacterium phlei!")
                                else:
                                    print("Input unclear. Try again.")
                            elif answer.lower().strip() == "negative" or answer.lower().strip() == "n":
                                answer = input("Your bacteria could be 1 of 2 bacteria in this key! What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                                if answer.lower().strip() == "red with zn":
                                    answer = input("Your bacteria is Listeria monocytogenes!")
                                elif answer.lower().strip() == "red with acids":
                                    answer = input("Your bacteria is Corynebacterium diptheria!")
                                else:
                                    print("Input unclear. Try again.")
                            else:
                                print("Input unclear. Try again.")
                        elif answer.lower().strip() == "double halo":
                            answer = input("Your bacteria could be 1 of 2 bacteria in this key! What is the result of your EYA test? (positive/negative)")
                            if answer.lower().strip() == "positive":
                                answer = input("Your bacteria is Bacillus cercus!")
                            elif answer.lower().strip() == "negative":
                                answer = input("Your bacteria is Bacillus subtillis!")
                            else:
                                print("Input unclear. Try again.")
                        else:
                            print("Input unclear. Try again.")
                    elif answer.lower().strip() == "negative":
                        answer = input("Your bacteria could be 1 of 2 in this key! What is the result of your EYA test? (positive/negative)")
                        if answer.lower().strip() == "positive":
                            answer = input("Your bacteria is Clostridium perfringens!")
                        elif answer.lower().strip() == "negative":
                            answer = input("Your bacteria is Clostridium sporogenes!")
                        else:
                            print("Input unclear. Try again.")
                    else:
                        print("Input unclear. Try again.")
                elif answer.lower().strip() == "cocci":
                    answer = input("Your bacteria could be 1 of 8 in this key. What is the result of your catalase test? (positive/negative)")
                    if answer.lower().strip() == "positive":
                        answer = input("Your bacteria could be 1 of 4 bacteria. What is the result of your MSA test? (yellow/pink)")
                        if answer.lower().strip() == "yellow" or answer.lower().strip() == "y":
                            answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                            if answer.lower().strip() == "red with zn":
                                answer = input("Your bacteria is Staphylococcus aureus!")
                            elif answer.lower().strip() == "red with acids":
                                answer = input("Your bacteria is Staphylococcus saprophyticus!")
                            else:
                                print("Input unclear. Try again.")
                        elif answer.lower().strip() == "pink" or answer.lower().strip() == "p":
                            answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                            if answer.lower().strip() == "red with zn":
                                answer = input("Your bacteria is Micrococcus luteus!")
                            elif answer.lower().strip() == "red with acids":
                                answer = input("Your bacteria is Staphylococcus epidermidis!")
                            else:
                                print("Input unclear. Try again.")
                        else:
                            print("Input unclear. Try again.")
                    elif answer.lower().strip() == "negative":
                        answer = input("Your bacteria could be 1 of 4 bacteria in this key. What is the result of your SBA test? (beta/gamma)")
                    else: 
                        print("Input unclear. Try again.")
                        if answer.lower().strip() == "beta":
                            answer = input("Your bacteria could be 1 of 3 bacteria in this key. What is the result of your DNase test? (positive/negative)")
                            if answer.lower().strip() == "positive":
                                answer = input("Your bacteria is Streptococcus pyogenes!")
                            elif answer.lower().strip() == "negative":
                                answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your mannitol fermentation test? (positive/negative)")
                                if answer.lower().strip() == "positive":
                                    answer = input("Your bacteria is Enterococcus faecalis!")
                                elif answer.lower().strip() == "negative":
                                    answer = input("Your bacteria is Streptococcus pneumoniae!")
                                else:
                                    print("Input unclear. Try again.")
                            else:
                                print("Input unclear. Try again.")
                        elif answer.lower().strip() == "gamma":
                            answer = input("Your bacteria is Streptococcus agalactiae!")
                        else:
                            print("Input unclear. Try again.")
                else:
                    print("Input unclear. Try again.")
            elif answer.lower().strip() == "negative":
                answer = input("This key is made for Gram positive bacteria. Try another key! :)")
            else:
                print("Input unclear. Try again.")


        elif answer.lower().strip() == "no" or answer.lower().strip():
            print("See you next time!")
        else:
            print("Input unclear. Try again.")
        key_start = input("Do you want to start over?")
# --------------------------------------------------
# def test_key():
#     """Test key"""
    
#     assert main()
#     answer = input("Would you like to determine an unknown bacteria? (yes/no)")
#     if answer.lower().strip() == "yes" or "y":
#         answer = input("Is your bacteria Gram positive or Gram negative? (positive/negative)")
#         if answer.lower().strip() == "positive" or "+" or "p":
#             answer = input("What is the morphology of your bacteria? (Bacilli/Cocci)")
#             if answer.lower().strip() == "bacilli" or "b":
#                 answer = input("Your bacteria could be 1 of 8 in this key. What is the result of your catalase test? (positive/negative)")
#                 if answer.lower().strip() == "positive" or "+" or "p":
#                     answer = input("Your bacteria could be 1 of 6 in this key. What is the result of your SBA? (alpha/gamma/double halo)")
#                     if answer.lower().strip() == "alpha" or "gamma" or "a" or "g":
#                         answer = input("Your bacteria could be 1 of 4 in this key. What is the result of your urease test? (positive/negative)")
#                         if answer.lower().strip() == "positive" or "+" or "p":
#                             answer = input("Your bacteria could be 1 of 2 bacteria in this key. What is the result of your CAMP test? (positive/negative)")
#                             if answer.lower().strip() == "positive" or "+" or "p":
#                                 answer = input("Your bacteria is Corynebacterium pseudotuberculosis!")

# --------------------------------------------------
if __name__ == '__main__':
    main()
