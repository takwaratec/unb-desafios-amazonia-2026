import re
import os

def extract_reviews(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for document sections: ## 📄 Filename
    # Followed by location, preview, etc. until the next --- or end of file
    sections = re.split(r'\n---', content)
    
    count = 0
    for section in sections:
        # Match the title header
        match = re.search(r'## 📄 (.*?)\n', section)
        if match:
            filename = match.group(1).strip()
            # Sanitize filename for filesystem
            safe_name = re.sub(r'[^\w\s\.-]', '_', filename).replace(' ', '_')
            if safe_name.endswith('.pdf'):
                safe_name = safe_name[:-4]
            
            output_path = os.path.join(output_dir, f'WTF_RES_{safe_name}.md')
            
            # Clean up the section content for an individual review file
            # Remove the icon and just keep the content
            clean_content = section.strip()
            
            # Add YAML frontmatter
            frontmatter = f"---\nproject: \"Mulheres Que Tecem a Floresta\"\nconsortium: \"UnB/UFAC/UFRR\"\ntype: \"Technical Review\"\nsource_file: \"{filename}\"\n---\n\n"
            
            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(frontmatter + clean_content)
            count += 1
            
    return count

if __name__ == "__main__":
    input_f = "04_PESQUISA_ANDAMENTO/SONDA_DOCLING/00_INVENTARIO_CURADORIA.md"
    out_d = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
    num = extract_reviews(input_f, out_d)
    print(f"Successfully extracted {num} reviews to {out_d}")
