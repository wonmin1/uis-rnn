# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from model.eval import sequence_acc


class TestSequenceAcc(unittest.TestCase):

  def test_mismatched_sequences(self):
    sequence1 = [0, 0, 1, 2, 2]
    sequence2 = [3, 3, 4, 4, 1]
    accuracy = sequence_acc(sequence1, sequence2)
    self.assertEqual(0.8, accuracy)

  def test_equivalent_sequences(self):
    sequence1 = [0, 0, 1, 2, 2]
    sequence2 = [3, 3, 4, 1, 1]
    accuracy = sequence_acc(sequence1, sequence2)
    self.assertEqual(1.0, accuracy)


if __name__ == '__main__':
  unittest.main()