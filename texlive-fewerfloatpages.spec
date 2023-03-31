Name:		texlive-fewerfloatpages
Version:	58058
Release:	2
Summary:	Reduce the number of unnecessary float pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fewerfloatpages
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements a float algorithm extension for
handling float pages. It attempts to reduce the number of
unnecessary (fairly empty) float pages while making sure that
floats nevertheless stay close to their call-outs. Several
aspects of the algorithm behavior are adjustable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fewerfloatpages
%{_texmfdistdir}/tex/latex/fewerfloatpages
%doc %{_texmfdistdir}/doc/latex/fewerfloatpages

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
