def read_requirements_file(filename):
    """Try different encodings to read the file"""
    encodings = ['utf-8', 'utf-16', 'utf-16le', 'utf-16be', 'ascii']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                return [line.strip() for line in f if line.strip() and not line.startswith('#')]
        except UnicodeDecodeError:
            continue
    
    raise ValueError(f"Could not read {filename} with any of the attempted encodings")

def update_requirements():
    # Read the pip freeze output
    try:
        frozen_lines = read_requirements_file('requirements1.txt')
        
        # Create dictionary of package versions
        frozen_reqs = {}
        for line in frozen_lines:
            if '==' in line:
                name, version = line.split('==', 1)
                frozen_reqs[name.strip().lower()] = version.strip()
                print(f"Found package: {name} with version: {version}")

        # Read original requirements
        original_reqs = read_requirements_file('requirements.txt')

        # Update versions for existing packages
        updated_reqs = []
        for req in original_reqs:
            # Handle packages with extras
            if '[' in req:
                package_name = req.split('[')[0].lower()
                extras = req[req.index('['):]
            else:
                package_name = req.lower()
                extras = ''

            # Remove any existing version specification
            package_name = package_name.split('==')[0].strip()
            
            if package_name in frozen_reqs:
                if extras:
                    # Preserve the original case of the package name
                    original_name = req.split('[')[0]
                    updated_reqs.append(f"{original_name}=={frozen_reqs[package_name]}{extras}")
                else:
                    # Preserve the original case of the package name
                    original_name = req.split('==')[0].strip()
                    updated_reqs.append(f"{original_name}=={frozen_reqs[package_name]}")
                print(f"Updated {package_name} to version {frozen_reqs[package_name]}")
            else:
                print(f"Warning: Version not found for {req}")
                updated_reqs.append(req)

        # Write updated requirements
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(updated_reqs) + '\n')
            
        print("\nUpdated requirements.txt successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    update_requirements()

