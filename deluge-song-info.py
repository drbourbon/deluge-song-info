#!/usr/bin/env python3
import logging
import argparse
import traceback
import datetime
import xml.etree.ElementTree as ET

try:
  # Try local import first.
  from pydel import pydel
except:
  import pydel

class SongInfo:
  def __init__(self, args):

    try:
      tree = ET.parse(args.input_file)
      root = tree.getroot()

      if root.tag != "song":
        logging.error("ERROR: Root tag is not 'song'.")
        raise Error()
    except:
      logging.error(
          "ERROR: Only songs from Deluge 3.x are supported. Try re-saving song using 3.x firmware."
      )
      print(traceback.format_exc())
      return

    self.project = pydel.Project.from_element(root)

  def project_length(self):
    tempo = self.project.tempo
    length = 0
    # Deluge instruments/tracks are stored bottom-to-top.
    for instrument in reversed(self.project.instruments):
#      print(instrument)
      for clip in instrument.clip_instances:
#        print(clip)
        end_in_seconds = pydel.pulses_to_seconds(clip.start+clip.length, 1)
        length = max(length, end_in_seconds)
    return length / tempo

  def tempo(self, args):
    print("{} bpm".format(int(float(self.project.tempo))))

  def key(self, args):
    print(self.project.rootTone)

  def duration(self, args):
    s = self.project_length()
    if(args.format):
      td = datetime.timedelta(seconds=s)
      print(td)
    else:
      print("{}s".format(s))

def main():
  parser = argparse.ArgumentParser(
      description="Extract info from Synthstrom Audible Deluge songs (XML)."
  )

  parser.add_argument('--verbose', help='be verbose', action="store_true")
  subparsers = parser.add_subparsers(help='sub-command help', dest="cmd")

  parser_tempo = subparsers.add_parser('tempo')

  parser_duration = subparsers.add_parser('duration')
  parser_duration.add_argument('--format', help='format song duration', action="store_true")

  parser_tempo = subparsers.add_parser('key')

  parser.add_argument(
      "input_file",
      type=argparse.FileType("r"),
      help="input Deluge .XML song file")

  args = parser.parse_args()

  logging.basicConfig(level=logging.ERROR)

  song = SongInfo(args)

  getattr(song, args.cmd)(args)
    
  #getinfo(args)


if __name__ == "__main__":
  main()
