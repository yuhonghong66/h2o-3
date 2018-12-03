from __future__ import print_function
import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
import time

def test_arrange_OOM():
    '''
    PUBDEV-5990 customer reported that h2o.arrange (sorting) takes way more memory than normal for sparse
    datasets of 1G.

    Thanks to Lauren DiPerna for finding the dataset to repo the problem.
    '''

    df = h2o.import_file(pyunit_utils.locate("bigdata/laptop/jira/sort_OOM.csv"))
    t1 = time.time()
    newFrame = df.sort("sort_col")
    print(newFrame[0,0])
    elapsed_time = time.time()-t1
    print("time taken to perform sort is {0}".format(elapsed_time))

    # check and make sure the sort columns contain the right value after sorting!
    answerFrame = h2o.import_file(pyunit_utils.locate("bigdata/laptop/jira/sort_OOM_answer.csv"))
    pyunit_utils.compare_frames_local(answerFrame, newFrame)

if __name__ == "__main__":
    pyunit_utils.standalone_test(test_arrange_OOM)
else:
    test_arrange_OOM()
