import streamlit as st


class Course(object):
    def __init__(self,code,name,level,credits,prereqs=[],coreqs=[],required=[],available=[],year='both',term=0):
        self.code = code
        self.name = name
        self.level=level
        self.credits=credits
        self.prereqs = prereqs
        self.coreqs = coreqs
        self.required=required
        self.available=available
        self.year=year
        self.term=term
    def __repr__(self):
        return self.name

    
catalog = [
    Course(1101,"Understanding Earth Sciences",
           1,20,
           required=['F600','F630','F665'],
           available=['F600','F630','F645','F665']),
    Course(1021,"Earth Materials",
           1,20,
           available=['F600','F665'],
           required=['F600']),
    Course(1111,"Environment, resources & materials",
           1,20,
           available=['F630','F645','F665'],
           required=['F630','F645']),
    Course(1141,'Sustainability',
           1,20,
           required=['F600','F630','F645','F665'],
           available=['F600','F630','F645','F665']),
    Course(1051,"Field Studies",
           1,20,
           required=['F600','F630','F665'],
           available=['F600','F630','F645','F665']),
    Course(91111,"Computing",
           1,20, 
           required=['F600','F630','F645','F665'],
           available=['F600','F630','F645','F665']),
    Course(1061,"Mathematical methods",
           1,20,
           required=[],
           available=['F600','F645','F630']),
    Course(1081,"Further mathematics",1,20,
           required=['F665'],
           available=['F600','F645','F665','F630']),
    Course(71261,"Introduction to climate change",1,20,required=['F645'],available=['F645']),
    Course(2031,"Sedimentary environments",
           2,20,
           prereqs=[1101],
           available=['F600','F630','F645','F665'],
           required=['F600','F630']),
    Course(2231,"Igneous & Met Processes",
           2,20,
           prereqs=[1021],
           available=['F600','F665'],
           required=['F600']),
    Course(2171,"Isotopes & Climate",
           2,20,
           available=['F600','F630','F645','F665'],
           required=['F630','F645']),
    Course(2191,"Fieldwork (geological)",
           2,20,
           available=['F600'],
           required=['F600']),
    Course(2201,"Fieldwork (environmental)",2,20,available=['F630','F645','F665'],required=['F630'],prereqs=[1051]),
    Course(2241,"Fieldwork (geophysical)",2,20,required=['F665'],available=['F630','F645','F665'],prereqs=[1051]),
    Course(2081,"Geophysical methods for geoscientists",
           2,20,
           required=['F665'],
           available=['F600','F630','F665']),
    Course(2291,"Geophysical Data Applications",2,20,required=['F665'],available=['F665']),
    Course(92117,"Geoinformatics",
           2,10,
           required=['F600','F630','F665'],
           term=1,
           available=['F600','F630','F645','F665']),
    Course(920111,
           "Structural geology",
           2,10,term=1,
           available=['F600','F630','F665'],
           required=['F600']),
    Course(923011,
           "Ancient life & environments",
           2,10,
           term=1,
           available=['F600','F630','F645','F665']),
    Course(72651,"Carbon & biogeochemical cycles",
           2,20,
           available=['F645']),
    Course(72571,"Reconstructing environmental change",
           2,20,
           available=['F645']),
    Course(72531,"Glaciers and glaciation",
           2,20,
           available=['F645']),
    Course(72661,"Climate change: geographical perspectives",
           2,20,
           available=['F645']),
    Course(83281,
           "Environmental management",
           2,20,
           coreqs=[2171],year='odd',
           available=['F600','F630','F645','F665'],required=['F630']),
    Course(3281,"Environmental management",3,20,prereqs=[2171],year='odd',available=['F600','F630','F645','F665'],required=['F630']),
    Course(2251,
           "Modelling Earth Processes",
           2,20,
           prereqs=[1081],
           year='odd',
           available=['F600','F630','F645','F665'],
           coreqs=[92117]),
    Course(82251,"Modelling Earth Processes",
           3,20,
           prereqs=[1081,92117],
           year='odd',
           available=['F600','F630','F645','F665']),
    Course(83357,"Tectonic processes & renewables",
           2,10,
           coreqs=[920111],
           year='odd',term=2,available=['F600','F630','F665']),
    Course(3357,"Tectonic processes & renewables",3,10,prereqs=[920111],year='odd',term=2,available=['F600','F630','F665']),
    Course(923012,"Frontiers in palaeo",
           2,10,coreqs=[923011],
           year='odd',
           term=2,
           available=['F600','F630','F645','F665']),
    Course(8923012,"Frontiers in palaeo",3,10,prereqs=[923011],year='odd',term=2,available=['F600','F630','F645','F665']),
    Course(83397,"Earth structure and dynamics",
           2,10,prereqs=[1081],year='odd',required=['F665'],term=2,available=['F600','F630','F665']),
    Course(3397,"Earth structure and dynamics",3,10,prereqs=[1081],year='odd',required=['F665'],term=2,available=['F600','F630','F665']),
    Course(83407,"Earth systems & climate II",
           2,10,year='odd',term=2,available=['F600','F630','F645','F665'],required=['F645']),
    Course(3407,"Earth systems & climate II",3,10,year='odd',term=2,available=['F600','F630','F645','F665'],required=['F645']),
    Course(94447,"Advanced geospatial modelling",
           2,10,
           year='odd',term=2,available=['F600','F630','F645','F665']),
    Course(894447,"Advanced geospatial modelling",3,10,year='odd',term=2,available=['F600','F630','F645','F665']),
    Course(83041,"Environmental geochemistry",
           2,20,coreqs=[2171],year='even',available=['F600','F630','F645','F665'],required=['F630']),
    Course(3041,"Environmental geochemistry",3,20,prereqs=[2171],year='even',available=['F600','F630','F645','F665'],required=['F630']),
    Course(83427,"Groundwater hydrology",
           2,10,year='even',term=2,available=['F600','F630','F645','F665']),
    Course(3427,"Groundwater hydrology",3,10,year='even',term=2,available=['F600','F630','F645','F665']),
    Course(920112,"Tectonics",2,10,coreqs=[920111],year='even',term=2,available=['F600','F630','F665'],required=['F600']),
    Course(8920112,"Tectonics",3,10,prereqs=[920111],year='even',term=2,available=['F600','F630','F665'],required=['F600']),
    Course(83417,"Astrobiology",2,10,year='even',term=2,available=['F600','F630','F645','F665']),
    Course(3417,"Astrobiology",3,10,year='even',term=2,available=['F600','F630','F645','F665']),
    Course(83327,"Earthquakes, sources and waves",2,10,prereqs=[1081],required=['F665'],year='even',term=1,available=['F600','F630','F665']),
    Course(3327,"Earthquakes, sources and waves",3,10,prereqs=[1081],required=['F665'],year='even',term=1,available=['F600','F630','F665']),
    Course(893337,"Seismics",2,10,prereqs=[1081],required=['F665'],year='even',term=2,available=['F600','F630','F665']),
    Course(93337,"Seismics",3,10,prereqs=[1081],required=['F665'],year='even',term=2,available=['F600','F630','F665']),
    Course(83447,"Earth systems & climate I",2,10,year='even',term=2,available=['F600','F630','F645','F665'],required=['F645']),
    Course(3447,"Earth systems & climate I",3,10,year='even',term=2,available=['F600','F630','F645','F665'],required=['F645']),
    Course(92557,"Resources",2,10,year='even',prereqs=[1021],term=2,available=['F600','F665']),
    Course(892557,"Resources",3,10,year='even',prereqs=[1021],term=2,available=['F600','F665']),
    Course(3022,"Dissertation",3,40,required=['F600','F630','F645','F665'],available=['F600','F630','F645','F665']),
    Course(3251,"Earth science into schools",3,20,available=['F600','F630','F665']),
    Course(930511,"Volcanic and magmatic processes",3,10,prereqs=[2231],term=1,available=['F600','F665']),
    Course(930512,"Volcanoes and environment",3,10,term=2,available=['F600','F630','F645','F665']),
    Course(3337,"Element cycling at subduction zones",3,10,prereqs=[2231],term=1,available=['F600','F665']),
    Course(93227,"Geochemistry of the Earth",3,10,prereqs=[2231],term=1,available=['F600','F665']),
    Course(3367,"West Alps field trip",3,10,prereqs=[2231],term=1,available=['F600','F665']),
    Course(33471,"Monitoring oceans",3,10,required=['F665'],term=1,available=['F600','F630','F645','F665']),
    Course(33472,"Geophysical flows",3,10,required=['F665'],term=2,available=['F600','F630','F665'],prereqs=[2251],year='even'),
    Course(833472,"Geophysical flows",3,10,required=['F665'],term=2,available=['F600','F630','F665'],coreqs=[82251],year='odd'),
    Course(3437,"Polar & Quaternary environmental processes",3,10,prereqs=[2171],term=1,available=['F600','F630','F645','F665']),
    Course(3387,"Atmospheric circulation and dynamics",3,10,term=1,available=['F600','F630','F645','F665']),
    Course(73927,"Past climate of low latitudes",3,10,term=1,available=['F645']),
    Course(73817,"Antarctic Environments",3,10,term=2,available=['F645']),
    Course(73191,"Sea level change & coastal evolution",3,20,available=['F645']),
    Course(73641,"Oceans past & present",3,20,available=['F645']),
    Course(73511,"Ice age environments",3,20,available=['F645']),
    Course(73641,"Archaeology and global sustainable developments",3,20,available=['F645'])


        


    
    
        
    
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

def contains(l,k):
    try:
        l.index(k)
        return True
    except ValueError:
        return False
    
def get_available_courses(catalog,prog,level,year=None):
    out = []
    for c in catalog:
        if contains(c.available,prog) and c.level == level:
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
#st.title("Geophysics")
sel_prog = st.radio("Programme:",["F600 Geology","F630 Environmental Geoscience",'F645 Climate Science',"F665 Geophysics"])
sel_year = st.radio("Level 1 Year is:",["Even","Odd"])
st.write("Select modules below. Once one year is 'complete', the next will become visible. After selecting all three years, a timetable will display at the bottom of this page.")
transcript = []
c1,c2,c3 = st.columns(3)
c1.write("Level 1")
c2.write("Level 2")
c3.write("Level 3")
yr=0 if sel_year == 'Even' else 1
prog = sel_prog.split(' ')[0]
l1 = get_available_courses(catalog,prog,1,year=yr)
sel_l1 = []
for c in l1:
    req=contains(c.required,prog)
    sel_l1+=[c1.checkbox("%s (%i)"%(c.name,c.credits),value=req,disabled=req)]
l1_credits = 0
for s,c in zip(sel_l1,l1):
    if s: 
        transcript+=[c.code]
        l1_credits+=c.credits
mathok=True
if not (contains(transcript,1061) or contains(transcript,1081)):
    c1.error("Must select one maths module")
    mathok=False
if contains(transcript,1061) and contains(transcript,1081):
    c1.error("Must select only one maths module")
    mathok=False
if not l1_credits==120:
    c1.error("Selected credits: %i"%l1_credits)
else:
    c1.success("Selected credits: %i"%l1_credits)
if l1_credits==120 and mathok:
    l2 = get_available_courses(catalog,prog,2,year=1-yr)
    sel_l2 = []
    for c in l2:
        has_prereqs=True
        for p in c.prereqs:
            try:
                transcript.index(p)
            except:
                has_prereqs=False
        req = contains(c.required,prog)
        sel_l2+=[c2.checkbox("%s (%i)"%(c.name,c.credits),value=req,disabled=req or not has_prereqs)]
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
            l3 = get_available_courses(catalog,prog,3,year=yr)
            sel_l3 = []
            for c in l3:
                has_prereqs=True
                for p in c.prereqs:
                    try:
                        transcript.index(p)
                    except:
                        has_prereqs=False
                req = contains(c.required,prog)
                sel_l3+=[c3.checkbox("%s (%i)"%(c.name,c.credits),value=req,disabled=req or not has_prereqs)]
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
                st.write("---")
                st.write("Timetable")
                terms = st.columns(6)
                for level in range(3):
                    for term in range(2):
                        terms[2*level+term].write("Level %i, Term %i"%(level+1,term+1))
                        terms[2*level+term].write("---")
                for c in chosen_courses:
                    if c.term==0 or c.term==1:
                        terms[2*(c.level-1)].write(c.name)
                    if c.term==0 or c.term==2:
                        terms[2*(c.level-1)+1].write(c.name)



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
        
