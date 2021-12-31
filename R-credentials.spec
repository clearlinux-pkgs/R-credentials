#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-credentials
Version  : 1.3.2
Release  : 4
URL      : https://cran.r-project.org/src/contrib/credentials_1.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/credentials_1.3.2.tar.gz
Summary  : Tools for Managing SSH and Git Credentials
Group    : Development/Tools
License  : MIT
Requires: R-askpass
Requires: R-curl
Requires: R-jsonlite
Requires: R-openssl
Requires: R-sys
BuildRequires : R-askpass
BuildRequires : R-curl
BuildRequires : R-jsonlite
BuildRequires : R-openssl
BuildRequires : R-sys
BuildRequires : buildreq-R

%description
other services. For HTTPS remotes the package interfaces the 'git-credential' 
    utility which 'git' uses to store HTTP usernames and passwords. For SSH 
    remotes we provide convenient functions to find or generate appropriate SSH 
    keys. The package both helps the user to setup a local git installation, and
    also provides a back-end for git/ssh client libraries to authenticate with 
    existing user credentials.

%prep
%setup -q -c -n credentials
cd %{_builddir}/credentials

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640993979

%install
export SOURCE_DATE_EPOCH=1640993979
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library credentials
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library credentials
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library credentials
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc credentials || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/credentials/DESCRIPTION
/usr/lib64/R/library/credentials/INDEX
/usr/lib64/R/library/credentials/LICENSE
/usr/lib64/R/library/credentials/Meta/Rd.rds
/usr/lib64/R/library/credentials/Meta/features.rds
/usr/lib64/R/library/credentials/Meta/hsearch.rds
/usr/lib64/R/library/credentials/Meta/links.rds
/usr/lib64/R/library/credentials/Meta/nsInfo.rds
/usr/lib64/R/library/credentials/Meta/package.rds
/usr/lib64/R/library/credentials/Meta/vignette.rds
/usr/lib64/R/library/credentials/NAMESPACE
/usr/lib64/R/library/credentials/NEWS
/usr/lib64/R/library/credentials/R/credentials
/usr/lib64/R/library/credentials/R/credentials.rdb
/usr/lib64/R/library/credentials/R/credentials.rdx
/usr/lib64/R/library/credentials/WORDLIST
/usr/lib64/R/library/credentials/ask_token.sh
/usr/lib64/R/library/credentials/doc/index.html
/usr/lib64/R/library/credentials/doc/intro.R
/usr/lib64/R/library/credentials/doc/intro.Rmd
/usr/lib64/R/library/credentials/doc/intro.html
/usr/lib64/R/library/credentials/help/AnIndex
/usr/lib64/R/library/credentials/help/aliases.rds
/usr/lib64/R/library/credentials/help/credentials.rdb
/usr/lib64/R/library/credentials/help/credentials.rdx
/usr/lib64/R/library/credentials/help/paths.rds
/usr/lib64/R/library/credentials/html/00Index.html
/usr/lib64/R/library/credentials/html/R.css
