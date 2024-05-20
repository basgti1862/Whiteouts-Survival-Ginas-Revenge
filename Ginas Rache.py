import cv2
import numpy as np
import pyautogui
import time
import os
import sys

# Pfad zu den Bilddateien (im gleichen Ordner wie das Skript)
script_dir = os.path.dirname(__file__)
horn_image_path = os.path.join(script_dir, 'horn_image.png')
rucksack_image_path = os.path.join(script_dir, 'rucksack_icon.png')
alles_icon_selected_path = os.path.join(script_dir, 'alles_icon_selected.png')
alles_icon_unselected_path = os.path.join(script_dir, 'alles_icon_unselected.png')
verwenden_image_path = os.path.join(script_dir, 'verwenden.png')
berserker_image_path = os.path.join(script_dir, 'berserker.png')
rally_image_path = os.path.join(script_dir, 'rally_aufrufen.png')
ausgleichen_image_path = os.path.join(script_dir, 'ausgleichen.png')
einsetzen_image_path = os.path.join(script_dir, 'einsetzen.png')
rally_aktiv_image_path = os.path.join(script_dir, 'RallyAktiv.png')
maschieren_image_path = os.path.join(script_dir, 'Maschieren.png')
ruckkehr_image_path = os.path.join(script_dir, 'Ruckkehr.png')

# Laden der Bilder in Graustufen
horn_image = cv2.imread(horn_image_path, cv2.IMREAD_GRAYSCALE)
rucksack_image = cv2.imread(rucksack_image_path, cv2.IMREAD_GRAYSCALE)
alles_icon_selected = cv2.imread(alles_icon_selected_path, cv2.IMREAD_GRAYSCALE)
alles_icon_unselected = cv2.imread(alles_icon_unselected_path, cv2.IMREAD_GRAYSCALE)
verwenden_image = cv2.imread(verwenden_image_path, cv2.IMREAD_GRAYSCALE)
berserker_image = cv2.imread(berserker_image_path, cv2.IMREAD_GRAYSCALE)
rally_image = cv2.imread(rally_image_path, cv2.IMREAD_GRAYSCALE)
ausgleichen_image = cv2.imread(ausgleichen_image_path, cv2.IMREAD_GRAYSCALE)
einsetzen_image = cv2.imread(einsetzen_image_path, cv2.IMREAD_GRAYSCALE)
rally_aktiv_image = cv2.imread(rally_aktiv_image_path, cv2.IMREAD_GRAYSCALE)
maschieren_image = cv2.imread(maschieren_image_path, cv2.IMREAD_GRAYSCALE)
ruckkehr_image = cv2.imread(ruckkehr_image_path, cv2.IMREAD_GRAYSCALE)

# Überprüfen, ob die Bilder korrekt geladen wurden
def check_images_loaded():
    if horn_image is None:
        print("Horn-Bild konnte nicht geladen werden.")
        return False
    if rucksack_image is None:
        print("Rucksack-Bild konnte nicht geladen werden.")
        return False
    if alles_icon_selected is None:
        print("Alles (ausgewählt) Bild konnte nicht geladen werden.")
        return False
    if alles_icon_unselected is None:
        print("Alles (nicht ausgewählt) Bild konnte nicht geladen werden.")
        return False
    if verwenden_image is None:
        print("Verwenden-Bild konnte nicht geladen werden.")
        return False
    if berserker_image is None:
        print("Berserker-Bild konnte nicht geladen werden.")
        return False
    if rally_image is None:
        print("Rally ausrufen-Bild konnte nicht geladen werden.")
        return False
    if ausgleichen_image is None:
        print("Ausgleichen-Bild konnte nicht geladen werden.")
        return False
    if einsetzen_image is None:
        print("Einsetzen-Bild konnte nicht geladen werden.")
        return False
    if rally_aktiv_image is None:
        print("RallyAktiv-Bild konnte nicht geladen werden.")
        return False
    if maschieren_image is None:
        print("Maschieren-Bild konnte nicht geladen werden.")
        return False
    if ruckkehr_image is None:
        print("Rückkehr-Bild konnte nicht geladen werden.")
        return False
    return True

# Funktion zum Auffinden eines Bildes auf dem Bildschirm mit verschiedenen Skalierungen
def find_image_on_screen(image, threshold=0.8, retries=3):
    if image is None:
        print("Bild konnte nicht geladen werden.")
        return None

    scales = [1.0, 0.9, 0.8, 1.1, 1.2]  # Verschiedene Skalierungen
    for _ in range(retries):
        for scale in scales:
            # Bild skalieren
            scaled_image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
            
            # Screenshot machen
            screen = pyautogui.screenshot()
            screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

            # Bildsuche mit OpenCV
            result = cv2.matchTemplate(screen, scaled_image, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val >= threshold:
                return max_loc
        time.sleep(1)  # Kurze Wartezeit vor erneutem Versuch

    return None

# Funktion zum Klicken auf eine Position
def click_on_position(position):
    if position is not None:
        x, y = position
        pyautogui.moveTo(x, y)
        pyautogui.click()

# Funktion zur Überprüfung, ob eines der drei Bilder auf dem Bildschirm ist
def any_of_three_images_present():
    rally_aktiv_position = find_image_on_screen(rally_aktiv_image, threshold=0.7, retries=1)
    maschieren_position = find_image_on_screen(maschieren_image, threshold=0.7, retries=1)
    ruckkehr_position = find_image_on_screen(ruckkehr_image, threshold=0.7, retries=1)

    # Debugging-Informationen ausgeben
    print(f"RallyAktiv Position: {rally_aktiv_position}")
    print(f"Maschieren Position: {maschieren_position}")
    print(f"Rückkehr Position: {ruckkehr_position}")

    return rally_aktiv_position is not None or maschieren_position is not None or ruckkehr_position is not None

# Hauptlogik
def main():
    # Überprüfen, ob alle Bilder korrekt geladen wurden
    if not check_images_loaded():
        return

    # Wartezeit, um das Programm zu starten und das Menü zu öffnen
    time.sleep(5)

    while True:
        print("Starte neuen Zyklus")
        
        # Menü "Rucksack" öffnen
        print("Öffne Menü 'Rucksack'")
        rucksack_position = find_image_on_screen(rucksack_image, threshold=0.7, retries=5)
        if rucksack_position:
            click_on_position(rucksack_position)
        else:
            print("Rucksacksymbol nicht gefunden.")
            main()  # Neustart des Skripts

        # Wartezeit, um sicherzustellen, dass das Menü geöffnet ist
        time.sleep(2)

        # "Alles"-Symbol suchen und darauf klicken, wenn es nicht ausgewählt ist
        print("Suche 'Alles'-Symbol und klicke darauf, wenn nicht ausgewählt")
        alles_position = find_image_on_screen(alles_icon_unselected, threshold=0.7, retries=5)
        if alles_position:
            click_on_position(alles_position)
            time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Symbol ausgewählt ist

        # Prüfen, ob das "Alles"-Symbol jetzt ausgewählt ist
        print("Prüfe, ob 'Alles'-Symbol ausgewählt ist")
        alles_selected_position = find_image_on_screen(alles_icon_selected, threshold=0.7, retries=5)
        if alles_selected_position:
            # Horn finden und darauf klicken
            print("Suche 'Horn'-Symbol und klicke darauf")
            horn_position = find_image_on_screen(horn_image, threshold=0.7, retries=5)
            if horn_position:
                click_on_position(horn_position)
                time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Horn ausgewählt ist

                # Verwenden-Symbol finden und darauf klicken
                print("Suche 'Verwenden'-Symbol und klicke darauf")
                verwenden_position = find_image_on_screen(verwenden_image, threshold=0.7, retries=5)
                if verwenden_position:
                    click_on_position(verwenden_position)
                    time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Symbol angeklickt ist
                    
                    # Berserker-Symbol finden und darauf klicken
                    print("Suche 'Berserker'-Symbol und klicke darauf")
                    berserker_position = find_image_on_screen(berserker_image, threshold=0.7, retries=5)
                    if berserker_position:
                        click_on_position(berserker_position)
                    else:
                        print("Berserker-Symbol nicht gefunden. Skript wird neu gestartet.")
                        main()  # Neustart des Skripts

                    time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Symbol angeklickt ist

                    # Rally ausrufen-Symbol finden und darauf klicken
                    print("Suche 'Rally ausrufen'-Symbol und klicke darauf")
                    rally_position = find_image_on_screen(rally_image, threshold=0.7, retries=5)
                    if rally_position:
                        click_on_position(rally_position)
                        time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Symbol angeklickt ist

                        # Ausgleichen-Symbol finden und darauf klicken
                        print("Suche 'Ausgleichen'-Symbol und klicke darauf")
                        ausgleichen_position = find_image_on_screen(ausgleichen_image, threshold=0.7, retries=5)
                        if ausgleichen_position:
                            click_on_position(ausgleichen_position)
                            time.sleep(2)  # Wartezeit, um sicherzustellen, dass das Symbol angeklickt ist

                            # Einsetzen-Symbol finden und darauf klicken
                            print("Suche 'Einsetzen'-Symbol und klicke darauf")
                            einsetzen_position = find_image_on_screen(einsetzen_image, threshold=0.7, retries=5)
                            if einsetzen_position:
                                click_on_position(einsetzen_position)
                            else:
                                print("Einsetzen-Symbol nicht gefunden.")
                        else:
                            print("Ausgleichen-Symbol nicht gefunden.")
                    else:
                        print("Rally ausrufen-Symbol nicht gefunden.")
                else:
                    print("Verwenden-Symbol nicht gefunden.")
            else:
                print("Horn-Symbol nicht gefunden. Skript wird gestoppt.")
                sys.exit()  # Skript stoppen
        else:
            print("Alles-Symbol konnte nicht ausgewählt werden.")

        # Wartezeit, bevor die Überprüfung erneut beginnt
        print("Warte 10 Sekunden, bevor die Überprüfung erneut beginnt")
        time.sleep(10)

        # Überprüfen, ob eines der drei Bilder auf dem Bildschirm ist
        while any_of_three_images_present():
            print("Mindestens eines der drei Bilder gefunden. Warte 10 Sekunden und überprüfe erneut.")
            time.sleep(10)  # Wartezeit, bevor erneut überprüft wird
        
        print("Keines der drei Bilder gefunden. Skript wird neu gestartet.")
        main()  # Neustart des Skripts

if __name__ == '__main__':
    main()
