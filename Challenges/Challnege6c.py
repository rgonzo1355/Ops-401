#!/bin/bash

# Rodolfo Gonzalez 
# January 16 2024

""" Resources:
https://github.com/subtropicalhorseback/scratchpad/blob/main/40106.sh
"""

#!/bin/bash

# Function to safely read user input
read_input() {
    read -p "$1" input  # Prompt the user for input with a custom message
    echo "$input"      # Return the user's input
}

# Function to create a new SFTP user
create_sftp_user() {
    local username="$1"  # Get the username from the function argument
    
    # Check if the group 'sftp_users' already exists
    if ! getent group sftp_users > /dev/null; then
        echo "Creating group 'sftp_users'."
        sudo groupadd sftp_users  # Create 'sftp_users' group if it doesn't exist
    else
        echo "Group 'sftp_users' already exists. Skipping creation."
    fi
    
    # Check if the user already exists
    if id "$username" &>/dev/null; then
        echo "User '$username' already exists. Skipping user creation."
    else
        echo "Creating user '$username'."
        sudo useradd -g sftp_users -m "$username"  # Create the user with 'sftp_users' group and home directory
        
        # Set a random password for the user (you can implement a more secure password generation)
        random_password=$(openssl rand -base64 12)  # Generate a random password
        echo "$username:$random_password" | sudo chpasswd  # Set the password for the user
        echo "Randomly generated password for $username: $random_password"
    fi
    
    # Create the user's SFTP directory
    echo "Creating SFTP directory for $username."
    sudo mkdir -p "/data/$username/upload"  # Create the directory
    
    # Set correct permissions on the user's SFTP directory
    sudo chown -R "$username:sftp_users" "/data/$username"  # Set ownership and group
}

# Function to add an SSH key for the user
add_ssh_key() {
    local username="$1"  # Get the username from the function argument
    local ssh_dir="/home/$username/.ssh"  # Define the user's .ssh directory
    
    # Check if the user has a public SSH key to provide
    read -p "Do you have a public SSH key to provide for the new user, $username? (y/n): " isKey
    
    if [ "$isKey" = 'y' ]; then 
        # Prompt for the public SSH key
        read -p "Provide the public SSH key for $username: " publickey
        
        # Create .ssh directory if it doesn't exist
        if [ ! -d "$ssh_dir" ]; then
            sudo mkdir -p "$ssh_dir"  # Create the .ssh directory
            sudo chown "$username:sftp_users" "$ssh_dir"  # Set ownership and group
        fi
        
        # Write the provided public key to authorized_keys with appropriate permissions
        echo "$publickey" | sudo tee "$ssh_dir/authorized_keys" > /dev/null  # Write the key
        sudo chmod 600 "$ssh_dir/authorized_keys"  # Set permissions
        sudo chown "$username:sftp_users" "$ssh_dir/authorized_keys"  # Set ownership
       
        echo -e "\nSuccessfully added public SSH key for $username.\n"
    else
        echo "Skipping SSH key setup for $username."
    fi
}

# Main script
main() {
    # Prompt for the username
    local username=$(read_input "Enter the username to enable for SFTP access on this server: ")
    
    # Create SFTP user and configure SSH
    create_sftp_user "$username"
    
    # Add SSH key if provided
    add_ssh_key "$username"
}

# Call the main function
main
