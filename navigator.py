import streamlit as st

class Course(object):
    def __init__(self,code,name,level,credits,prereqs=[],coreqs=[],required=False,year='both',term=0):
        self.code = code
        self.name = name
        self.level=level
        self.credits=credits
        self.prereqs = prereqs
        self.coreqs = coreqs
        self.required=required
        self.year=year
        self.term=term
    def __repr__(self):
        return self.name

    
catalog = [
    Course(1101,"Understanding Earth Sciences",1,20,required=True),
    Course(1021,"Earth Materials",1,20,required=False),
    Course(1111,"Environment, resources & materials",1,20,required=False),
    Course(1141,'Sustainability',1,20,required=True),
    Course(1051,"Field Studies",1,20,required=True),
    Course(1991,"Computing",1,20, required=True),
    Course(1081,"Further mathematics",1,20,required=True),
    Course(2031,"Sedimentary environments",2,20),
    Course(2231,"Igneous & Met Processes",2,20,prereqs=[1021]),
    Course(2171,"Isotopes & Climate",2,20),
    Course(2201,"Fieldwork (environmental)",2,20),
    Course(2241,"Fieldwork (geophysical)",2,20,required=True),
    Course(2081,"Geophysical methods for geoscientists",2,20,required=True),
    Course(2291,"Geophysical Data Applications",2,20,required=True),
    Course(2997,"Geoinformatics",2,10,required=True),
    Course(20119,"Structural geology",2,10),
    Course(23019,"Ancient life & environments",2,10),
    Course(2281,"Environmental management",2,20,coreqs=[2171],year='odd'),
    Course(2551,"Modelling Earth Processes",2,20,prereqs=[1081],year='odd'),
    Course(2357,"Tectonic processes & renewables",2,10,prereqs=[20119],year='odd'),
    Course(23010,"Frontiers in palaeo",2,10,prereqs=[23019],year='odd'),
    Course(2397,"Earth structure and dynamics",2,10,prereqs=[1081],year='odd',required=True),
    Course(2407,"Earth systems & climate II",2,10,year='odd'),
    Course(9997,"Advanced geospatial modelling",2,10,year='odd'),
    Course(2041,"Environmental geochemistry",2,20,coreqs=[2171],year='even'),
    Course(2422,"Groundwater hydrology",2,10,year='even'),
    Course(20110,"Tectonics",2,10,prereqs=[20119],year='even'),
    Course(2417,"Astrobiology",2,10,year='even'),
    Course(2327,"Earthquakes, sources and waves",2,10,prereqs=[1081],required=True,year='even'),
    Course(2007,"Seismics",2,10,prereqs=[1081],required=True,year='even'),
    Course(2447,"Earth systems & climate I",2,10,year='even'),
    Course(2887,"Resources",2,10,year='even',prereqs=[1021]),
    Course(3022,"Dissertation",3,40,required=True),
    Course(3251,"Earth science into schools",3,20),
    Course(30519,"Volcanic and magmatic processes",3,10,prereqs=[2231]),
    Course(30510,"Volcanoes and environment",3,10),
    Course(3337,"Element cycling at subduction zones",3,10,prereqs=[2231]),
    Course(3997,"Geochemistry of the Earth",3,10,prereqs=[2231]),
    Course(3367,"West Alps field trip",3,10,prereqs=[2231]),
    Course(3368,"Monitoring oceans",3,10,required=True),
    Course(3347,"Geophysical flows",3,10,required=True),
    Course(3437,"Polar & Quaternary environmental processes",3,10,prereqs=[2171]),
    Course(3387,"Atmospheric circulation and dynamics",3,10),
    Course(3281,"Environmental management",3,20,prereqs=[2171],year='odd'),
    Course(3551,"Modelling Earth Processes",3,20,prereqs=[1081],year='odd'),
    Course(3357,"Tectonic processes & renewables",3,10,prereqs=[20119],year='odd'),
    Course(33010,"Frontiers in palaeo",3,10,prereqs=[23019],year='odd'),
    Course(3397,"Earth structure and dynamics",3,10,prereqs=[1081],year='odd',required=True),
    Course(3407,"Earth systems & climate II",3,10,year='odd'),
    Course(8997,"Advanced geospatial modelling",3,10,year='odd'),
    Course(3041,"Environmental geochemistry",3,20,prereqs=[2171],year='even'),
    Course(3422,"Groundwater hydrology",3,10,year='even'),
    Course(30110,"Tectonics",3,10,prereqs=[20119],year='even'),
    Course(3417,"Astrobiology",3,10,year='even'),
    Course(3327,"Earthquakes, sources and waves",3,10,prereqs=[1081],required=True,year='even'),
    Course(3007,"Seismics",3,10,prereqs=[1081],required=True,year='even'),
    Course(3447,"Earth systems & climate I",3,10,year='even'),
    Course(3887,"Resources",3,10,year='even',prereqs=[1021]),
]

def find(catalog,code):
    for c in catalog:
        if c.code==code:
            return c
    return None

def split_compulsory(catalog):
    req=[]
    notreq=[]
    for c in catalog:
        if c.required:
            req+=[c]
        else:
            notreq+=[c]
    return req,notreq

def count_credits(catalog):
    credits = 0
    for c in catalog:
        credits+=c.credits
    return credits

def get_available_courses(catalog,level,year=None):
    out = []
    for c in catalog:
        if c.level == level:
            if (year is None) or (year==0 and (c.year=='both' or c.year=='even')) or (year==1 and (c.year=='both' or c.year=='odd')):
                out +=[c]
    return out

def apply_prereqs(catalog,transcript):
    out = []
    for c in catalog:
        ok = True
        for p in c.prereqs:
            try:
                transcript.index(p)
            except:
                ok = False
        if ok: out+=[c]
    return out

st.set_page_config(layout='wide')
st.title("Geophysics")
sel_year = st.radio("Level 1 Year is:",["Even","Odd"])
transcript = []
c1,c2,c3 = st.columns(3)
yr=0 if sel_year is 'Even' else 1
l1 = get_available_courses(catalog,1,year=yr)
sel_l1 = []
for c in l1:
    sel_l1+=[c1.checkbox("%s (%i)"%(c.name,c.credits),value=c.required,disabled=c.required)]
l1_credits = 0
for s,c in zip(sel_l1,l1):
    if s: 
        transcript+=[c.code]
        l1_credits+=c.credits
if not l1_credits==120:
    c1.error("Selected credits: %i"%l1_credits)
else:
    c1.success("Selected credits: %i"%l1_credits)
if l1_credits==120:
    l2 = get_available_courses(catalog,2,year=1-yr)
    sel_l2 = []
    for c in l2:
        has_prereqs=True
        for p in c.prereqs:
            try:
                transcript.index(p)
            except:
                has_prereqs=False
        sel_l2+=[c2.checkbox("%s (%i)"%(c.name,c.credits),value=c.required,disabled=c.required or not has_prereqs)]
    l2_credits = 0
    coreqs = []
    for s,c in zip(sel_l2,l2):
        if s: 
            transcript+=[c.code]
            coreqs+=c.coreqs
            l2_credits+=c.credits
    has_coreqs = True
    for c in coreqs:
        try:
            transcript.index(c)
        except:
            c2.error("Corequisite not selected: %s"%find(l2,c))
            has_coreqs=False
    if not l2_credits == 120:
        c2.error("Selected credits: %i"%l2_credits)
    else:
        c2.success("Selected credits: %i"%l2_credits)
        if has_coreqs:
            l3 = get_available_courses(catalog,3,year=yr)
            sel_l3 = []
            for c in l3:
                has_prereqs=True
                for p in c.prereqs:
                    try:
                        transcript.index(p)
                    except:
                        has_prereqs=False
                sel_l3+=[c3.checkbox("%s (%i)"%(c.name,c.credits),value=c.required,disabled=c.required or not has_prereqs)]
            l3_credits = 0
            for s,c in zip(sel_l3,l3):
                if s:
                    transcript+=[c.code]
                    coreqs+=c.coreqs
                    l3_credits+=c.credits
            has_coreqs = True
            for c in coreqs:
                try:
                    transcript.index(c)
                except:
                    c3.error("Corequisite not selected: %s"%find(l3,c))
                    has_coreqs=False
            if not l3_credits == 120:
                c3.error("Selected credits: %i"%l3_credits)
            else:
                c3.success("Selected credits: %i"%l3_credits)
                if has_coreqs:
                    chosen_courses = []
                    for c in transcript:
                        chosen_courses+=[find(catalog,c)]
                
                t1,t2,t3 = st.columns(3)
                [t1.write(c) for c in get_available_courses(chosen_courses,1)]


# while True:
#     year = input("Enter calendar year of entry: ")
#     try:
#         if int(year)%2==0:
#             year = 0
#         else:
#             year = 1
#         break
#     except:
#         pass
# print("Level One")
# l1 = get_available_courses(catalog,1,year=year)
# selected = []
# required,optional = split_compulsory(l1)
# print("   REQUIRED:")
# credits = 0
# for course in required:
#     selected+=[course.code]
#     credits+=course.credits
#     print("      %s (%i)"%(course.name,course.credits))

# while 120-credits>0:
#     print("   Credits remaining: %i"%(120-credits))
#     print("   Choose an option:")
#     for i,course in enumerate(optional):
#         print("      %i %s (%i)"%(i+1,course.name,course.credits))
#     while True:
#         choice = input("      Enter a number: ")
#         try:
#             choice=int(choice)-1
#             break
#         except:
#             pass
#     course = optional[choice]
#     selected+=[course.code]
#     credits+=course.credits
#     optional.pop(choice)

# print()
# year = 1-year
# print("Level Two")
# l2 = get_available_courses(catalog,2,year=year)
# l2 = apply_prereqs(l2,selected)
# required,optional = split_compulsory(l2)
# print("   REQUIRED:")
# credits = 0
# for course in required:
#     selected+=[course.code]
#     credits+=course.credits
#     print("      %s (%i)"%(course.name,course.credits))
# while 120-credits>0:
#     print("   Credits remaining: %i"%(120-credits))
#     print("   Choose an option:")
#     for i,course in enumerate(optional):
#         print("      %i %s (%i)"%(i+1,course.name,course.credits))
#     while True:
#         choice = input("      Enter a number: ")
#         try:
#             choice=int(choice)-1
#             break
#         except:
#             pass
#     course = optional[choice]
#     selected+=[course.code]
#     credits+=course.credits
#     optional.pop(choice)
#     for coreq in course.coreqs:
#         try:
#             selected.index(coreq)
#         except:
#             coreq_course = find(catalog,coreq)
#             print("Adding co-requisite: %s"%coreq_course.name)
#             selected+=[coreq_course.code]
#             credits+=coreq_course.credits
#             optional.pop(optional.index(coreq_course))
#     if credits>120: raise InputError("Too many credits!")
#     print()
# year = 1-year
# print("Level Three")
# l2 = get_available_courses(catalog,3,year=year)
# l2 = apply_prereqs(l2,selected)
# required,optional = split_compulsory(l2)
# print("   REQUIRED:")
# credits = 0
# for course in required:
#     selected+=[course.code]
#     credits+=course.credits
#     print("      %s (%i)"%(course.name,course.credits))
# while 120-credits>0:
#     print("   Credits remaining: %i"%(120-credits))
#     print("   Choose an option:")
#     for i,course in enumerate(optional):
#         print("      %i %s (%i)"%(i+1,course.name,course.credits))
#     while True:
#         choice = input("      Enter a number: ")
#         try:
#             choice=int(choice)-1
#             break
#         except:
#             pass
#     course = optional[choice]
#     selected+=[course.code]
#     credits+=course.credits
#     optional.pop(choice)
#     for coreq in course.coreqs:
#         try:
#             selected.index(coreq)
#         except:
#             coreq_course = find(catalog,coreq)
#             print("Adding co-requisite: %s"%coreq_course.name)
#             selected+=[coreq_course.code]
#             credits+=coreq_course.credits
#             optional.pop(optional.index(coreq_course))
#     if credits>120: raise ValueError("Too many credits!")

# programme = []
# for selection in selected:
#     programme+=[find(catalog,selection)]

# print()
# for i in range(1,4):
#     print("Level %i"%i)
#     for c in get_available_courses(programme,i):
#         print(c)
        
