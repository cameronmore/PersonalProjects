import json
import json
import jsonschema

def Chicago_bib_author_block(item):
    """
    Component of SerializeFromJSON that handles authors in the Chicago style for bibliographic entries (not notes). It has as an input a JSON instance that conforms to the Media Elements Schema and returns a well-formatted author entry.
    """
    item = item
    author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName'])
    if "author2" in item.keys():
        author_string = author_string + " and " + str(item['author2']['firstName']) + " " + str(item['author2']['lastName'])
        if "author3" in item.keys():
            author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + ", " + str(item['author2']['lastName']) + ", " + str(item['author2']['firstName']) + ", and " + str(item['author3']['firstName']) + " " + str(item['author3']['lastName'])
    author_string = author_string + ". "
    return author_string

def Chicago_bib_translator_block(item):
    """
    Component of SerializeFromJSON that takes a JSON instance of a Media Element Schema and returns the Chicago style bibliographic entry portion of translators for a piece of media.
    """
    item=item
    
    translator_string= ""
    if "translator" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + ". "
    if "translator2" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + " and " +str(item['translator2']['firstName']) + " "  + str(item['translator2']['lastName']) + ". "
    if "translator3" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + ", " + str(item['translator2']['firstName']) + " "  + str(item['translator2']['lastName']) + ", and " + str(item['translator3']['firstName']) + " "  + str(item['translator3']['lastName']) + ". "
        
    return translator_string


def Chicago_bib_editor_block(item):
    """
    Component of SerializeFromJSON that takes a JSON instance of a Media Element Schema and returns the Chicago style bibliographic entry portion of editor for a piece of media.
    """
    item=item
    
    editor_string= ""
    if "editor" in item.keys():
        editor_string = "Edited by " + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + ". "
    if "editor2" in item.keys():
        editor_string = "Edited by " + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + " and " +str(item['editor2']['firstName']) + " "  + str(item['editor2']['lastName']) + ". "
    if "editor3" in item.keys():
        editor_string = "Edited by " + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + ", " + str(item['editor2']['firstName']) + " "  + str(item['editor2']['lastName']) + ", and " + str(item['editor3']['firstName']) + " "  + str(item['editor3']['lastName']) + ". "
        
    return editor_string

def MLA_bib_author_block(item):
    """
    Component of SerializeFromJSON for authors in MLA.
    """
    item=item
    author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + ". "
    if "author2" in item.keys():
        author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + " and " + str(item['author2']['firstName']) + " " + str(item['author2']['lastName'])
        if "author3" in item.keys():
            author_string = str(item['author']['lastName']) + ", et al. "
    
    return author_string

def MLA_bib_translator_block(item):
    """
    Component of SerializeFromJSON that takes a JSON instance of a Media Element Schema and returns the Chicago style bibliographic entry portion of translators for a piece of media.
    """
    item=item
    
    translator_string= ""
    end = ""
    if "editor" in item.keys():
        end = ", "
    if "translator" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + end
    if "translator2" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + " and " +str(item['translator2']['firstName']) + " "  + str(item['translator2']['lastName']) + end
    if "translator3" in item.keys():
        translator_string = "Translated by " + str(item['translator']['firstName']) + " "  + str(item['translator']['lastName']) + ", " + str(item['translator2']['firstName']) + " "  + str(item['translator2']['lastName']) + ", and " + str(item['translator3']['firstName']) + " "  + str(item['translator3']['lastName']) + end
        
    return translator_string  


def MLA_bib_editor_block(item):
    """
    Component of SerializeFromJSON that takes a JSON instance of a Media Element Schema and returns the Chicago style bibliographic entry portion of editor for a piece of media.
    """
    item=item
    
    editor_string= ""
    beginning="Edited by "
    if "editor" in item.keys():
        beginning="edited by "
    if "translator" in item.keys():
        end="."
    if "editor" in item.keys():
        editor_string = beginning + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + ". "
    if "editor2" in item.keys():
        editor_string = beginning + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + " and " +str(item['editor2']['firstName']) + " "  + str(item['editor2']['lastName']) + ". "
    if "editor3" in item.keys():
        editor_string = beginning + str(item['editor']['firstName']) + " "  + str(item['editor']['lastName']) + ", " + str(item['editor2']['firstName']) + " "  + str(item['editor2']['lastName']) + ", and " + str(item['editor3']['firstName']) + " "  + str(item['editor3']['lastName']) + ". "
        
    return editor_string

def MLA_bib_director_block(item):
    """
    Component of SerializeFromJSON that takes a JSON instance of a Media Element Schema and returns the Chicago style bibliographic entry portion of editor for a piece of media.
    """
    item=item
    
    editor_string= ""
    beginning="Directed by "
    if "author" in item.keys():
        editor_string = beginning + str(item['author']['firstName']) + " "  + str(item['author']['lastName']) + ", "
    if "author2" in item.keys():
        editor_string = beginning + str(item['author']['firstName']) + " "  + str(item['author']['lastName']) + " and " +str(item['author2']['firstName']) + " "  + str(item['author2']['lastName']) + ", "
    if "author3" in item.keys():
        director_string = beginning + str(item['author']['firstName']) + " "  + str(item['author']['lastName']) + ", " + str(item['author2']['firstName']) + " "  + str(item['author2']['lastName']) + ", and " + str(item['author3']['firstName']) + " "  + str(item['author3']['lastName']) + ", "
        
    return director_string

def PageLength(item):
    """
    Component of SerializeFromJSON() to grab the page numbers for a text.
    """
    item=item
    page_string = str(item['length']['firstPage']) + "-" + str(item['length']['lastPage'])
    if str(item['length']['firstPage']) == str(item['length']['lastPage']):
        page_string = str(item['length']['firstPage'])
    
    return page_string
    pass

def SerializeFromJSON(input_file=str,style=str,skip_missing=bool,update_existing=bool):
    """
    This function is designed to take a JSON Media Element type object as an input and produce bibliographic citations in a standard format \n
    Currently, the style options include "MLA" and "Chicago" \n
    The skip_missing boolean will skip required elements for media citations if False, but throw an error if True or None. \n
    The update_existing flag will update the existing JSON file with the citations in-line and not produce a new output. \n
    Valid media types include: book, book with only editors, article, chapter in book, film, webpage with author, webpage without author. \n
    The script can handle Chicago format for: 'book', 'film', 'article', 'webpage without author', 'webpage with author', and 'chapter in book'. And MLA for 'book', 'chapter in book', 'film', 'webpage with author', and 'webpage without author'\n
    Limitations: handles only up to three editors and authors, less translators, a small amount of source types, and only Chicago style.
    """
    with open(input_file) as f:
        input_file = json.load(f)
    style=style

    for item in input_file["mediaData"]:
        
        # Chicago style
        if style == "Chicago":
            if item['mediaType'] == "book":
                
                author_string = Chicago_bib_author_block(item)
                
                translator_string= Chicago_bib_translator_block(item)
                
                title_string = str(item['title'] + ". ")
                    
                editor_string = Chicago_bib_editor_block(item)

                publisher_string = str(item['publisher']['location']) + ": " + str(item['publisher']['publisherName']) + ", " + str(item['time']['year']) + ". "
                
                citation_string = author_string +  title_string + translator_string + editor_string +publisher_string
                
                print(citation_string)
                
            if item['mediaType'] == "chapter in book":
                
                # Author block
                author_string = Chicago_bib_author_block(item)
                
                title_string = str(item['title'] + ". ")
                
                editedVolume_string = str(item['editedVolume'] + ", ")
                editor_string = str(item['editor']['firstName']) + " " + str(item['editor']['lastName'])
                if "editor2" in item.keys():
                    editor_string = editor_string + " and " + str(item['editor2']['firstName']) + " " + str(item['editor2']['lastName'])
                    if "editor3" in item.keys():
                        editor_string = str(item['editor']['lastName']) + ", " + str(item['editor']['firstName']) + ", " + str(item['editor2']['lastName']) + ", " + str(item['editor2']['firstName']) + ", and " + str(item['editor3']['firstName']) + " " + str(item['editor3']['lastName'])
                editor_string = editor_string + ", "  
                length_string = ""              
                publisher_string = str(item['publisher']['location']) + ": " + str(item['publisher']['publisherName']) + ", " + str(item['time']['year']) + ". "
                
                length_string = ""
                if "length" in item.keys():
                    length_string =  str(item['length']['firstPage']) + "-" + str(item['length']['lastPage']) + ". "
                
                """Harris, Muriel. “Talk to Me: Engaging Reluctant Writers.” In A Tutor’s Guide: Helping Writers One to One, edited by Ben Rafoth, 24-34. New Hampshire: Heinemann, 2000."""
                citation_string = author_string + title_string + "In " + editedVolume_string + "edited by " + editor_string + length_string + publisher_string
                print(citation_string)
                pass
                    
            if item['mediaType'] == "webpage without author":
                
                title_string = '"' + str(item['title']) + '." '
                publisher_string = str(item['publisher']['publisherName']) + ". "
                accessed_string = "Accessed at " + str(item['accessDate']) + ". "
                url_string = str(item['url']) + "."
                citation_string = publisher_string + title_string + accessed_string + url_string
                print(citation_string)
                pass
            
            if item['mediaType'] == "article":
                
                #Author Block
                author_string = Chicago_bib_author_block(item)
                
                translator_string= Chicago_bib_translator_block(item)
                
                title_string = '"' + str(item['title']) + '." '
                
                journal_string = ""
                if "journal" in item.keys():
                    journal_string = str(item['journal']['journalName']) + " " + str(item['journal']['volume']) + ", no. " + str(item['journal']['issue']) + ": "
                    if "time" in item.keys():
                        if "year" in item['time']:
                            journal_string = str(item['journal']['journalName']) + " " + str(item['journal']['volume']) + ", no. " + str(item['journal']['issue']) + " (" +str(item['time']['year']) + "): "
                
                length_string = ""
                if "length" in item.keys():
                    length_string =  str(item['length']['firstPage']) + "-" + str(item['length']['lastPage']) + ". "
                
                doi_string = ""
                if "doi" in item.keys():
                    doi_string = str(item['doi']) + ". "

                citation_string = author_string +  title_string + translator_string + journal_string + length_string + doi_string
                
                print(citation_string)
                
            if item['mediaType'] == "webpage with author":
                
                # Chicago Author Block
                author_string = Chicago_bib_author_block(item)
                
                accessed_string = "Accessed at " + str(item['accessDate']) + ". "                
                
                time_string = ""
                if 'time' in item.keys():
                    accessed_string = ""
                    if "year" in item['time'].keys():
                        time_string = str(item['time']['year'] + ". ")
                    if "day" in item['time'].keys():
                        time_string = str(item['time']['month'] + " " + item['time']['day'] + ", " + item['time']['year'] + ". ")
                        
                title_string = '"' + str(item['title']) + '." '
                publisher_string = str(item['publisher']['publisherName']) + ". "
                url_string = str(item['url']) + "."
                citation_string = author_string  + title_string + publisher_string + time_string + accessed_string + url_string
                print(citation_string)

                
            if item['mediaType'] == "film":
                
                # Author block
                author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + ", director. "
                if "author2" in item.keys():
                    author_end = ", directors. "
                    author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + " and " + str(item['author2']['firstName']) + " " + str(item['author2']['lastName']) + author_end
                    if "author3" in item.keys():
                        author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + ", " + str(item['author2']['lastName']) + ", " + str(item['author2']['firstName']) + ", and " + str(item['author3']['firstName']) + " " + str(item['author3']['lastName']) + author_end

                length_string = ""
                if "length" in item.keys():
                    hr_string = " hr. "
                    if int(item['length']['duration']['hours']) > 1:
                        hr_string = " hrs. "
                    
                    length_string =  str(item['length']['duration']['hours']) + hr_string +str(item['length']['duration']['minutes']) +  " min. "                
                
                title_string = str(item['title'] + ". ")
                
                publisher_string =  str(item['publisher']['publisherName']) + ", "
                
                year_string = str(item['time']['year']) + ". "
                
                doi_string = ""
                if "doi" in item.keys():
                    doi_string = str(item['doi']) + ". "
                
                citation_string = author_string + title_string + publisher_string + year_string + length_string  + url_string + doi_string
                print(citation_string)
        
        # MLA style
        if style == "MLA":
            
            if item['mediaType'] == "chapter in book":
                
                # MLA Author block
                author_string = MLA_bib_author_block(item)
                
                title_string = str('"' + item['title'] +  '." ' )
                
                editedVolume_string = str(item['editedVolume'] + ", ")
                editor_string = str(item['editor']['firstName']) + " " + str(item['editor']['lastName'])
                if "editor2" in item.keys():
                    editor_string = editor_string + " and " + str(item['editor2']['firstName']) + " " + str(item['editor2']['lastName'])
                    if "editor3" in item.keys():
                        editor_string = str(item['editor']['lastName']) + ", et al. "
                editor_string = editor_string + ", "  
                length_string = ""
                publisher_string = str(item['publisher']['publisherName']) + ", " + str(item['time']['year']) + ". "
                
                length_string = ""
                if "length" in item.keys():
                    length_string =  str(item['length']['firstPage']) + "-" + str(item['length']['lastPage']) + ". "
                
                """Harris, Muriel. “Talk to Me: Engaging Reluctant Writers.” In A Tutor’s Guide: Helping Writers One to One, edited by Ben Rafoth, 24-34. New Hampshire: Heinemann, 2000."""
                citation_string = author_string + title_string + editedVolume_string + "edited by " + editor_string +  publisher_string + "pp. " + length_string
                print(citation_string)
                pass
            
            if item['mediaType'] == "webpage without author":
                
                time_string = ""
                if 'time' in item.keys():
                    if "year" in item['time'].keys():
                        time_string = str(item['time']['year'] + ", ")
                    if "day" in item['time'].keys():
                        time_string = str(item['time']['day'] + " " + item['time']['month'] + " " + item['time']['year'] + ", ")
                    
                title_string = '"' + str(item['title']) + '." '
                publisher_string = str(item['publisher']['publisherName']) + ", "
                accessed_string = " Accessed at " + str(item['accessDate']) + ". "
                url_string = str(item['url']) + "."
                
                citation_string =  title_string + publisher_string + time_string + url_string + accessed_string
                print(citation_string)

            if item['mediaType'] == "webpage with author":
                
                # MLA Author block
                author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + ". "
                if "author2" in item.keys():
                    author_string = str(item['author']['lastName']) + ", " + str(item['author']['firstName']) + " and " + str(item['author2']['firstName']) + " " + str(item['author2']['lastName'])
                    if "author3" in item.keys():
                        author_string = str(item['author']['lastName']) + ", et al. "                
                time_string = ""
                if 'time' in item.keys():
                    if "year" in item['time'].keys():
                        time_string = str(item['time']['year'] + ", ")
                    if "day" in item['time'].keys():
                        time_string = str(item['time']['day'] + " " + item['time']['month'] + " " + item['time']['year'] + ", ")
                    
                title_string = '"' + str(item['title']) + '." '
                publisher_string = str(item['publisher']['publisherName']) + ", "
                accessed_string = " Accessed at " + str(item['accessDate']) + ". "
                url_string = str(item['url']) + "."
                citation_string =  author_string = title_string + publisher_string + time_string + url_string + accessed_string
                print(citation_string)
                pass
            
            if item['mediaType'] == "book":
                
                author_string = MLA_bib_author_block(item)
                
                title_string =  str(item['title']) + '. '
                
                translator_string = MLA_bib_translator_block(item)
                
                editor_string = MLA_bib_editor_block(item)
                
                publisher_string = str(item['publisher']['publisherName']) + ", " + str(item['time']['year'])
                
                citation_string = author_string + title_string + translator_string + editor_string + publisher_string
                print(citation_string)
            
            if item['mediaType'] == "article":
                
                author_string = MLA_bib_author_block(item)
                
                title_string = '"' + str(item['title']) + '." '
                
                page_string = PageLength(item)
                
                journal_string = ""
                if "journal" in item.keys():
                    journal_string = str(item['journal']['journalName']) + ", vol. " + str(item['journal']['volume']) + ", no. " + str(item['journal']['issue']) + ", pp. "
                    if "time" in item.keys():
                        if "year" in item['time']:
                            journal_string = str(item['journal']['journalName']) + ", vol. " + str(item['journal']['volume']) + ", no. " + str(item['journal']['issue']) + ", " + str(item['time']['year']) + ", pp. "
                
                citation_string = author_string + title_string + journal_string + page_string + ". "
                print(citation_string)
            
            if item['mediaType'] == "film":
                title_string = str(item['title']) + '. '
                author_string = "Directed by " + str(MLA_bib_director_block(item))
                publisher_string = str(item['publisher']['publisherName'] + ", " + item['time']['year'] + ". ")
                
                citation_string = title_string + author_string + publisher_string
                
                print(citation_string)
                
            

SerializeFromJSON("MediaElementSchema/Schema/Sample.json","MLA")

