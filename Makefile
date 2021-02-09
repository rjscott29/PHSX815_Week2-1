# C++ compiler
CXX = g++ 

# Paths to the folders with the necessary header files for compilation
CXX += -I/Users/christopherrogan/GitHub/matplotlib-cpp/
CXX += -I/usr/local/Cellar/python\@3.9/3.9.1_6/Frameworks/Python.framework/Versions/3.9/include/python3.9/
CXX += -I/usr/local/lib/python3.9/site-packages/numpy/core/include

# Path to the folder with the Python shared library
GLIBS =  -L/usr/local/Cellar/python\@3.9/3.9.1_6/Frameworks/Python.framework/Versions/3.9/lib/
# Flag to let the compiler know which shared library to use
GLIBS += -lpython3.9

# some compiler flags
CXXFLAGS = -std=c++11

# location of source code
SRCDIR = ./src/

#location of header files
INCLUDEDIR = ./include/

CXX += -I$(INCLUDEDIR)

# location of object files (from compiled library files)
OUTOBJ = ./obj/

CC_FILES := $(wildcard src/*.cc)
HH_FILES := $(wildcard include/*.hh)
OBJ_FILES := $(addprefix $(OUTOBJ),$(notdir $(CC_FILES:.cc=.o)))

# targets to make
all: CoinToss.x CoinAnalysis.x

# recipe for building CoinToss.x
CoinToss.x:  $(SRCDIR)CoinToss.C $(OBJ_FILES) $(HH_FILES)
	$(CXX) $(CXXFLAGS) -o CoinToss.x $(OUTOBJ)/*.o $(GLIBS) $ $<
	touch CoinToss.x

# recipe for building CoinAnalysis.x
CoinAnalysis.x:  $(SRCDIR)CoinAnalysis.C $(OBJ_FILES) $(HH_FILES)
	$(CXX) $(CXXFLAGS) -o CoinAnalysis.x $(OUTOBJ)/*.o $(GLIBS) $ $<
	touch CoinAnalysis.x

$(OUTOBJ)%.o: src/%.cc include/%.hh
	$(CXX) $(CXXFLAGS) -c $< -o $@

# clean-up target (make clean)
clean:
	rm -f *.x
	rm -rf *.dSYM
	rm -f $(OUTOBJ)*.o
