%global tl_name fewerfloatpages
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0b
Release:	%{tl_revision}.1
Summary:	Reduce the number of unnecessary float pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fewerfloatpages
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fewerfloatpages.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements a float algorithm extension for handling float
pages. It attempts to reduce the number of unnecessary (fairly empty)
float pages while making sure that floats nevertheless stay close to
their call-outs. Several aspects of the algorithm behavior are
adjustable.

