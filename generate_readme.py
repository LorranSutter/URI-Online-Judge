import os

# Categories mapping to their emoji and the extensions to count.
# We count .py files for all categories, and .sql / .py for SQL.
CATEGORIES = [
    ("Beginner", "🔰", [".py"]),
    ("Ad-Hoc", "⚙️", [".py"]),
    ("Geometry", "📐", [".py"]),
    ("Mathematics", "🔢", [".py"]),
    ("SQL", "🗄️", [".sql", ".py"]),
    ("Strings", "🔤", [".py"]),
    ("Structures", "🧱", [".py"]),
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(base_dir, "README.md")
    
    total_solved = 0
    category_counts = {}
    
    for category, emoji, extensions in CATEGORIES:
        category_dir = os.path.join(base_dir, category)
        count = 0
        if os.path.isdir(category_dir):
            for filename in os.listdir(category_dir):
                name, ext = os.path.splitext(filename)
                if ext in extensions and name.isdigit():
                    count += 1
        category_counts[category] = count
        total_solved += count

    # Generate the badge content
    start_marker = "<!-- SUMMARY:START -->"
    end_marker = "<!-- SUMMARY:END -->"
    summary_content = f"{start_marker}[![Solved Challenges](https://img.shields.io/badge/Solved%20Challenges-{total_solved}-brightgreen?style=for-the-badge&logo=python&logoColor=white)](https://www.beecrowd.com.br/){end_marker}"

    # Read the README.md file
    if not os.path.exists(readme_path):
        print(f"Error: README.md not found at {readme_path}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    if start_marker not in readme_content or end_marker not in readme_content:
        print("Error: Could not find SUMMARY:START and/or SUMMARY:END markers in README.md")
        return

    parts = readme_content.split(start_marker)
    sub_parts = parts[1].split(end_marker)
    
    new_readme_content = f"{parts[0]}{summary_content}{sub_parts[1]}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme_content)

    print(f"Success: README.md updated with progress summary. Total solved: {total_solved} problems.")

if __name__ == "__main__":
    main()
