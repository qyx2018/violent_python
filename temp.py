import optparse
parser = optparse.OptionParser()
parser.add_option('-c', '--child', dest = 'age', action = 'store_const', const = 0)
parser.add_option('-a', '--adult', dest = 'age', action = 'store_const', const = 1)
parser.add_option('-e', '--elder', dest = 'age', action = 'store_const', const = 2)

age_list = ['child', 'adult', 'elder']
(options, args) = parser.parse_args()

print ('You are a(an)', age_list[options.age])