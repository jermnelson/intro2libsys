"""
 Collection of misc. functions for assiting development of the 
 Intro2LibSys DLS and MOOC.

"""
__author__ = "Jeremy Nelson"

def add_author(given, family, birth=None, death=None, idloc=None):
    author = {'givenName':given,
              'familyName':family}
    if birth is not None:
        author['birthDate'] = birth
    if death is not None:
        author['deathDate'] = death
    if idloc is not None:
        author['idloc:uri'] = idloc
    return author

def creative_work(type_of=None):
    doc = {"@context": {"@vocab": "http://schema.org/",
                        "idloc": "http://id.loc.gov"}}
    if type_of is not None:
        doc['@type'] = type_of
    return doc

schema_cwrks = {"WebPage": "http://schema.org/WebPage",
                "BlogPosting": "http://schema.org/BlogPosting",
                "NewsArticle": "http://schema.org/NewsArticle",
                "ScholarlyArticle":"http://schema.org/ScholarlyArticle",
                "TechArticle":"http://schema.org/TechArticle",
                "Book": "http://schema.org/Book",
                "VideoObject": "http://schema.org/VideoObject"}
            
online_keys = schema_cwrks.keys()
counter = 3                
for row in readings[5:]:
    fields = row.get('fields')
    question_title = raw_input(r"Keep {0}?".format(fields.get('title')))
    if question_title.lower() == 'y':
        open_in_tab = raw_input("Open in tab? (y|n)")
        if open_in_tab.lower() == 'y':
            if fields.get('url') is not None:
                webbrowser.open_new_tab(fields.get('url'))
        print("Please select type-of Creative Work")
        for count, key in enumerate(online_keys):
            print("\t{0} {1}".format(count, key))
        online_type = raw_input(r">> ")
        online_key = online_keys[int(online_type)]
        creative_work = utilities.creative_work(type_of=schema_cwrks.get(online_key))
        creative_work['name'] = fields.get('title')
        counter += 1
        creative_work['@id'] = 'http://intro2libsys.info/resource/{0}'.format(counter)
        if fields.get('url') is not None:
            creative_work['url'] = fields.get('url')
        if online_key == "Book":
            bookFormats = ['Hardcover', 'Paperback', 'EBook']
            print("Select bookFormat")
            for i, name in enumerate(bookFormats):
                print("\t{0} {1}".format(i,name))
            book_format = raw_input(r">> ")
            creative_work["bookFormat"] = bookFormats[int(book_format)]
        while 1:
            author_prompt = raw_input(r"Add author? (y|n)")
            if author_prompt.lower() == 'y':
                author_info = {}
                author_info['givenName'] = raw_input(r"givenName >>")
                author_info['familyName'] = raw_input(r"familyName >>")
                loc_prompt = raw_input(r"Has loc-id? (y|n)")
                if loc_prompt.lower() == 'y':
                    author_info['idloc:url'] = raw_input(r"idloc:url >>")
                
                if creative_work.has_key("author"):
                    if type(creative_work['author']) is not list:
                        authors = creative_work.pop('author')
                        creative_work['authors'] = [authors,]
                    creative_work['authors'].append(author_info)
                else:
                    creative_work['authors'] = [author_info,]
            else:
                break
        json_filename = raw_input(r"Enter json filename >>")
        json.dump(creative_work,
                  open("C:\\Users\\jernelson\\Development\\intro2libsys\\intro2libsys\\syllabus\\fixures\\{0}.json".format(json_filename),
                       "wb"),
                  indent=2,
                  sort_keys=True)

