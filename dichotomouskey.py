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

    answer = input("Would you like to determine an unknown bacteria? (yes/no)")

    if answer.lower().strip() == "yes":
        answer = input("Is your bacteria Gram positive or Gram negative? (positive/negative)")
        if answer.lower().strip() == "positive":
            answer = input("What is the morphology of your bacteria? (Bacilli/Cocci)")
            if answer.lower().strip() == "bacilli":
                answer = input("Your bacteria could be 1 of 8 in this key. What is the result of your catalase test? (positive/negative)")
                if answer.lower().strip() == "positive":
                    answer = input("Your bacteria could be 1 of 6 in this key. What is the result of your SBA? (alpha/gamma/double halo)")
                    if answer.lower().strip() == "alpha" or "gamma":
                        answer = input("Your bacteria could be 1 of 4 in this key. What is the result of your urease test? (positive/negative)")
                        if answer.lower().strip() == "positive":
                            answer = input("Your bacteria could be 1 of 2 bacteria in this key. What is the result of your CAMP test? (positive/negative)")
                            if answer.lower().strip() == "positive":
                                answer = input("Your bacteria is Corynebacterium pseudotuberculosis!")
                            elif answer.lower().strip() == "negative":
                                answer = input("Your bacteria is Mycobacterium phlei!")
                        elif answer.lower().strip() == "negative":
                            answer = input("Your bacteria could be 1 of 2 bacteria in this key! What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                            if answer.lower().strip() == "red with zn":
                                answer = input("Your bacteria is Listeria monocytogenes!")
                            elif answer.lower().strip() == "red with acids":
                                answer = input("Your bacteria is Corynebacterium diptheria!")
                    elif answer.lower().strip() == "double halo":
                        answer = input("Your bacteria could be 1 of 2 bacteria in this key! What is the result of your EYA test? (positive/negative)")
                        if answer.lower().strip() == "positive":
                            answer = input("Your bacteria is Bacillus cercus!")
                        elif answer.lower().strip() == "negative":
                            answer = input("Your bacteria is Bacillus subtillis!")
                elif answer.lower().strip() == "negative":
                    answer = input("Your bacteria could be 1 of 2 in this key! What is the result of your EYA test? (positive/negative)")
                    if answer.lower().strip() == "positive":
                        answer = input("Your bacteria is Clostridium perfringens!")
                    elif answer.lower().strip() == "negative":
                        answer = input("Your bacteria is Clostridium sporogenes!")
            elif answer.lower().strip() == "cocci":
                answer = input("Your bacteria could be 1 of 8 in this key. What is the result of your catalase test? (positive/negative)")
                if answer == "positive":
                    answer = input("Your bacteria could be 1 of 4 bacteria. What is the result of your MSA test? (yellow/pink)")
                    if answer == "yellow":
                        answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                        if answer == "red with zn":
                            answer = input("Your bacteria is Staphylococcus aureus!")
                        elif answer == "red with acids":
                            answer = input("Your bacteria is Staphylococcus saprophyticus!")
                    elif answer == "pink":
                        answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your nitrate test? (Red with Zn/Red with Acids)")
                        if answer == "red with zn":
                            answer = input("Your bacteria is Micrococcus luteus!")
                        elif answer == "red with acids":
                            answer = input("Your bacteria is Staphylococcus epidermidis!")
                elif answer == "negative":
                    answer = input("Your bacteria could be 1 of 4 bacteria in this key. What is the result of your SBA test? (alpha/beta/gamma)")
                    if answer == "alpha" or "beta":
                        answer = input("Your bacteria could be 1 of 3 bacteria in this key. What is the result of your DNase test? (positive/negative)")
                        if answer == "positive":
                            answer = input("Your bacteria is Streptococcus pyogenes!")
                        elif answer == "negative":
                            answer = input("Your bacteria could be 1 of 2 bacteria. What is the result of your mannitol fermentation test? (positive/negative)")
                            if answer == "positive":
                                answer = input("Your bacteria is Enterococcus faecalis!")
                            elif answer == "negative":
                                answer = input("Your bacteria is Streptococcus pneumoniae!")
                    elif answer == "gamma":
                        answer = input("Your bacteria is Streptococcus agalactiae!")
        elif answer.lower().strip() == "negative":
            answer = input("This key is made for Gram positive bacteria. Try another key! :)")


    else:
        print("See you next time!")
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
