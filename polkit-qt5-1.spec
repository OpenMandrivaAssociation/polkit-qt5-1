%define major 1

Summary:	Library that allows developer to access PolicyKit-1 API
Name:		polkit-qt5-1
Version:	0.103.1
Release:	4
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0: 	%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	polkit-1-devel >= 0.98.1
BuildRequires:	qt5-devel >= 5.1.0

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------
%define libpolkit_qt5_core_1 %mklibname polkit-qt5-core-1_ %{major}

%package -n %{libpolkit_qt5_core_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-core-10 < %{version}-%{release}

%description -n %{libpolkit_qt5_core_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_core_1}
%{_libdir}/libpolkit-qt5-core-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt5_gui_1 %mklibname polkit-qt5-gui-1_ %{major}

%package -n %{libpolkit_qt5_gui_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-gui-10 < %{version}-%{release}

%description -n %{libpolkit_qt5_gui_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_gui_1}
%{_libdir}/libpolkit-qt5-gui-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt5_agent_1 %mklibname polkit-qt5-agent-1_ %{major}

%package -n %{libpolkit_qt5_agent_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-agent-10 < %{version}-%{release}

%description -n %{libpolkit_qt5_agent_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_agent_1}
%{_libdir}/libpolkit-qt5-agent-1.so.%{major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:	Devel stuff for polkit-Qt
Group:		Development/KDE and Qt
Requires:	%{libpolkit_qt5_core_1} = %{version}-%{release}
Requires:	%{libpolkit_qt5_gui_1} = %{version}-%{release}
Requires:	%{libpolkit_qt5_agent_1} = %{version}-%{release}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/polkit-qt-1
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/cmake/PolkitQt5-1/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt5 
%make

%install
%makeinstall_std -C build

