#!/usr/bin/env ruby
# It accepts one argument and pass it to a regular expression matching method
puts ARGV[0].scan(/hbt{2,5}n/).join
