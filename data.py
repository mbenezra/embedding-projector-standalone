import numpy as np
import calendar
np.savetxt('vectors.tsv', np.random.rand(7,100), delimiter='\t', fmt="%f")
np.savetxt('metadata.tsv', np.asarray(calendar.day_name), delimiter='\t', fmt="%s")