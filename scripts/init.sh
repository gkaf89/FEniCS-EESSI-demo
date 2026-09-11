#!/bin/bash --login

declare eb_var=""
for eb_var in $(env | grep -E '^EASYBUILD_' | cut -d= -f1); do
    unset "${eb_var}"
done

module --force purge
module load EESSI/2025.06
module load EESSI-extend
