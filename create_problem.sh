#!/bin/bash

# Ensure two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <category> <problem_number>"
    exit 1
fi

category_arg="$1"
problem_number="$2"

# Validate that the problem number consists only of digits
if [[ ! "$problem_number" =~ ^[0-9]+$ ]]; then
    echo "Error: Problem number must consist only of digits."
    exit 1
fi

# Normalize and validate category
lower_cat=$(echo "$category_arg" | tr '[:upper:]' '[:lower:]')
is_tried=false
sub_category_lower="$lower_cat"

if [[ "$lower_cat" =~ ^tried/(.*)$ ]]; then
    is_tried=true
    sub_category_lower="${BASH_REMATCH[1]}"
fi

case "$sub_category_lower" in
    ad-hoc)         normalized_sub="Ad-Hoc" ;;
    beginner)       normalized_sub="Beginner" ;;
    geometry)       normalized_sub="Geometry" ;;
    mathematics)    normalized_sub="Mathematics" ;;
    sql)            normalized_sub="SQL" ;;
    strings)        normalized_sub="Strings" ;;
    structures)     normalized_sub="Structures" ;;
    *)
        echo "Error: Invalid category '$category_arg'."
        echo "Category must be one of: Ad-Hoc, Beginner, Geometry, Mathematics, SQL, Strings, Structures (optionally prefixed with Tried/)"
        exit 1
        ;;
esac

if [ "$is_tried" = true ]; then
    normalized_category="Tried/$normalized_sub"
else
    normalized_category="$normalized_sub"
fi

# Ensure the directory exists
mkdir -p "$normalized_category"

# Compute the file path
file_path="${normalized_category}/${problem_number}.py"

# Check if file already exists
if [ -f "$file_path" ]; then
    echo "Error: File '$file_path' already exists."
    exit 1
fi

# Write starter template
cat << EOF > "$file_path"
# Problem: ${problem_number} - ${normalized_category}
# URI Online Judge

def main():
    pass

if __name__ == '__main__':
    main()
EOF

echo "Success: Created template at '$file_path'"
